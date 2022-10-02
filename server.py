
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

import json
import pandas as pd
from collections import Counter
import shortuuid

f = open('newdata.json')
data = json.load(f)
# {'time': 1664339224992, 'userId': 1, 'platform': 'android', 'position': [168.97, 100.03, -411.21], 'country': 'CN', 'events': {'ping': 1}}


'''
users = []
for d in data:
    users.append(d['userId'])

counts = dict(Counter(users))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)
'''


### AGGREGATE EVENT DATA BY USERID
user_events = {}
for d in data:
    if d['userId'] not in user_events.keys():
        user_events[d['userId']] = d['events']
    else:
        e = user_events[d['userId']].copy()
        for event, count in d['events'].items():
            if event in e.keys():
                e[event] += 1
            else:
                e[event] = 1
        user_events[d['userId']] = e.copy()


df = pd.DataFrame(user_events)
df.columns = df.iloc[0]
df = df[1:]
df = df.T

df['max'] = df.max(axis = 1)
df['max_event'] = df.apply(lambda row: row[row == df.columns[row.argmax()]].index.tolist(), axis = 1)
stats = df.describe()
# print(df.head(15))
# print(stats)

# print("hand held sum", df.sum(axis=0))

df_json = df.to_json(orient = 'table')
parsed_json = json.loads(df_json)
data = parsed_json["data"]


#from data
total_players = {
        "messages": "522",
        "messages_rank": "1583",
        "country_number": "200",
        "ping_number": "919",
        "ping_rank": "1583",
        "holding_hands_number": "107",
        "holding_hands_rank": "1583"
    }
lookup_table = {}
long_names = ["panda", "acorn", "time", "carrot", "square", "round", "table", "chair", "telephone"]
index = 0
for item in data:
    name = str(index) + long_names[index%len(long_names)]
    item["name"] = name
    for column in item:
        if item[column] == None:
            item[column] = 0
    item["messages_rank"] = (int(item["chat_msg"]) / int(total_players["messages"])) * 1583
    item["ping_rank"] =  (int(item["got_wax"]) / int(total_players["ping_number"])) * 1583
    item["holding_hands_rank"] = (int(item["hand_held"]) / int(total_players["holding_hands_number"]))* 1583
    lookup_table[name] = index
    index += 1

#print(lookup_table)
# data = [
#     {
#         "name": "alfred",
#         "messages": "1000",
#         "messages_rank": "25",
#         "country": "USA",
#         "country_percentage": "1",
#         "ping_number": "10",
#         "ping_rank": "1002",
#         "holding_hands_number": "235",
#         "holding_hands_rank": "2"
#     },
#     {
#         "name": "stuart",
#         "messages": "234",
#         "messages_rank": "2343",
#         "country": "Germany",
#         "country_percentage": "4",
#         "ping_number": "255",
#         "ping_rank": "1005",
#         "holding_hands_number": "22",
#         "holding_hands_rank": "2000"
#     }
# ]

print(data[0])

#lookup_table = {"alfred": 0, "stuart": 1}

@app.route('/', methods=['GET', 'POST'])
def home():
    global data
    return render_template("home.html", data = data)

@app.route('/search/<player_name>', methods=['GET', 'POST'])
def search_for_player(player_name=None):
    global data
    global total_players

    index = -1
    my_data = []
    if player_name != None:
        if player_name in lookup_table.keys():
            index = lookup_table[player_name]
            my_data = data[index]
    print('my data is', my_data)
    return render_template("player.html", player_data=my_data, total=total_players)

if __name__ == '__main__':
   app.run(debug = True)
