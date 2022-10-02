
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

total_players = {
        "messages": "10000",
        "messages_rank": "5000",
        "country_number": "200",
        "ping_number": "5000",
        "ping_rank": "5000",
        "holding_hands_number": "1000",
        "holding_hands_rank": "5000"
    }

data = [
    {
        "name": "alfred",
        "messages": "1000",
        "messages_rank": "25",
        "country": "USA",
        "country_percentage": "1",
        "ping_number": "10",
        "ping_rank": "1002",
        "holding_hands_number": "235",
        "holding_hands_rank": "2"
    },
    {
        "name": "stuart",
        "messages": "234",
        "messages_rank": "2343",
        "country": "Germany",
        "country_percentage": "4",
        "ping_number": "255",
        "ping_rank": "1005",
        "holding_hands_number": "22",
        "holding_hands_rank": "2000"
    }
]

lookup_table = {"alfred": 0, "stuart": 1}

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
    return render_template("player.html", player_data=my_data, total=total_players)

if __name__ == '__main__':
   app.run(debug = True)
