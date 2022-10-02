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
print(df.head(15))
print(stats)

print("hand held sum", df.sum(axis=0))

df_json = df.to_json(orient = 'table')
parsed_json = json.loads(df_json)
all_data = parsed_json["data"]

for item in all_data:
    item["name"] = shortuuid.uuid()

print(all_data[0])


# i = 0
# for item in parsed_json["data"]:
#     print(item)
#     if i == 10:
#         break
#     i+=1