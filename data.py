import json
import pandas as pd
from collections import Counter

f = open('dawn-event-data.json')
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
print(df.head(15))
df = df.set_index('userId')
df['max'] = df.max(axis = 1)
df['max_event'] = df.apply(lambda row: row[row == df.columns[row.argmax()]].index.tolist(), axis = 1)
df.describe()