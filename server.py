
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

import json
import pandas as pd
from collections import Counter
import shortuuid

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


df = pd.DataFrame(user_events).T
#df.columns = df.iloc[0]
#df = df[1:]
#df = df.T

df['max'] = df.max(axis = 1)
df['max_event'] = df.idxmax(axis = 1)
#df['max_event'] = df.apply(lambda row: df.columns[row[row == df.columns[row.argmax()]].index], axis = 1)
stats = df.describe()
print(df.head(15))
print(stats)

print("Sum \n", df.sum(axis=0))

df_json = df.to_json(orient = 'table')
parsed_json = json.loads(df_json)
all_data = parsed_json["data"]

for item in all_data:
    item["name"] = shortuuid.uuid()

print(all_data[1])

# SUMS
totals = df.sum(axis = 0)
maxs = df.max()
mins = df.min()
means = df.mean()
medians = df.median()
stds = df.std()


total_players = {
        "messages": totals['chat_msg'],
        "messages_rank": means['chat_msg'],
        "ping_number": totals['ping'],
        'ping_rank': means['ping'],
        "wax_number": totals['got_wax'],
        'wax_rank': means['got_wax'],
        #'wingbuff': totals['wingbuff_collect'],
        #'wingbuff_rank': means['wingbuff_collect'],
        #'spirit_shop': totals['spirit_shop_item_purchased'],
        #'spirit_rank': means['spirit_shop_item_purchased'],
        "holding_hands_number": totals['hand_held'],
        'holding_hands_rank': means['hand_held']
    }
lookup_table = {}
# long_names = ["panda", "acorn", "time", "carrot", "square", "round", "table", "chair", "telephone"]
index = 0
for item in all_data:
    name = str(index)
    item["name"] = name
    if 'chat_msg' not in item.keys():
        item['chat_msg'] = 0
    if 'events' in item.keys():
        if 'ping' in item['events'].keys():
            item['ping'] = item['events']['ping']
        else:
            item['ping'] = 0
        if 'hand_held' not in item.keys():
            item['hand_held'] = 0
        if 'got_wax' not in item.keys():
            item['got_wax'] = 0
    for column in item:
        if item[column] == None:
            item[column] = 0
    item["messages_rank"] = item['chat_msg']
    item["ping_rank"] =  item['ping']
    item["holding_hands_rank"] = item['hand_held']
    item["wax_rank"] = item['got_wax']
    lookup_table[name] = index
    index += 1

print("data is \n", all_data[4])

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

print(all_data[0])

#lookup_table = {"alfred": 0, "stuart": 1}

@app.route('/', methods=['GET', 'POST'])
def home():
    global all_data
    return render_template("home.html", data = all_data)

@app.route('/search/<player_name>', methods=['GET', 'POST'])
def search_for_player(player_name=None):
    global all_data
    global total_players

    index = -1
    my_data = []
    if player_name != None:
        if player_name in lookup_table.keys():
            index = lookup_table[player_name]
            my_data = all_data[index]
    print('my data is', my_data)
    return render_template("player.html", player_data=my_data, total=total_players)

if __name__ == '__main__':
   app.run(debug = True)
