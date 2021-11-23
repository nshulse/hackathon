from __future__ import annotations
from flask import Flask, render_template, request
from requests import get  # This function is how we will make requests to a server.
from requests.models import Response  # This is the type of a Response object.
from random import randint
from helpers import check_answer
from typing import Union



class Player:
    name: str
    weight: int
    stats: dict 


    def __init__(self, name, weight, stats):
        self.name = name
        self.weight = weight
        self.stats = stats


    def __repr__(self):
        return f"{self.name} {self.weight} {self.stats}"


    def test(self):
        print("wadsadadsa")
        Player.name = "pwepaw"
        Player.weight = 69


    def new_p(self) -> None:
        print("wtf")
        player_one_id: int = randint(1, 400)
        bball_api_response: Response = get(f"https://www.balldontlie.io/api/v1/players/{player_one_id}")
        bball_api_response_data = bball_api_response.json()
        self.weight = bball_api_response_data['weight_pounds']
        big_weight = bball_api_response_data['weight_pounds']
        self.name = f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}"
        big_name = f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}"
        bball_averages_response: Response = get(f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_one_id}")
        bball_averages_data = bball_averages_response.json()
        self.stats = bball_averages_data['data'][0]
        big_stats = bball_averages_data['data'][0]
        while len(bball_averages_data['data']) == []:
            player_one_id: int = randint(1, 400)
            bball_api_response: Response = get(f"https://www.balldontlie.io/api/v1/players/{player_one_id}")
            bball_api_response_data = bball_api_response.json()
            self.weight = bball_api_response_data['weight_pounds']
            big_weight = bball_api_response_data['weight_pounds']
            self.name = (f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}")
            big_name = f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}"
            bball_averages_response: Response = get(f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_one_id}")
            bball_averages_data = bball_averages_response.json()
            self.stats = bball_averages_data['data'][0]
            big_stats = bball_averages_data['data'][0]


def get_player():
    player_one_id: int = randint(1, 400)
    bball_api_response: Response = get(f"https://www.balldontlie.io/api/v1/players/{player_one_id}")
    bball_api_response_data = bball_api_response.json()
    #self.weight = bball_api_response_data['weight_pounds']
    big_weight = bball_api_response_data['weight_pounds']
    #self.name = f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}"
    big_name = f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}"
    bball_averages_response: Response = get(f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_one_id}")
    bball_averages_data = bball_averages_response.json()
    #self.stats = bball_averages_data['data'][0]
    #big_stats = bball_averages_data['data'][0]
    while (bball_averages_data['data']) == []:
        player_one_id: int = randint(1, 400)
        bball_api_response: Response = get(f"https://www.balldontlie.io/api/v1/players/{player_one_id}")
        bball_api_response_data = bball_api_response.json()
        #self.weight = bball_api_response_data['weight_pounds']
        big_weight = bball_api_response_data['weight_pounds']
        #self.name = (f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}")
        big_name = f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}"
        bball_averages_response: Response = get(f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_one_id}")
        bball_averages_data = bball_averages_response.json()
        #self.stats = bball_averages_data['data'][0]
    big_stats = bball_averages_data['data'][0]
    return Player(big_name, big_weight, big_stats)


player_one = get_player()
player_two = get_player()

print(player_one)
print(player_two)

#player_one: Player = Player(big_name, big_weight, big_stats)
#print(player_one)


from flask import Flask, render_template, request
from requests import get  # This function is how we will make requests to a server.
from requests.models import Response  # This is the type of a Response object.
from random import randint
from helpers import check_answer

app: Flask = Flask(__name__)

p1 = 0
p2 = 1
player_points = 0
p1_weight = 0
p2_weight = 0


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/game', methods=["GET", "POST"])
def game():
    global p1, p2, player_points, p1_weight, p2_weight
    if request.method == "GET":
        player_one_list = random_player_name()
        player_two_list = random_player_name()
        p1 = player_one_list[0]
        p1_weight = player_one.weight
        p2 = player_two_list[0]
        p2_weight = player_two.weight
        #player_points: int = 0
        #while p1_weight == None:
            #p1 = random_player_name()
        #while p2_weight == None:
            #p2 = random_player_name()
        #while p2_weight == p1_weight:
            #p2 = random_player_name()
        #p1_weight = int(p1_weight)
        #p2_weight = int(p2_weight)
    if request.method == "POST":
        player: str = request.form["player"]
        x = check_answer(player, p1_weight ,p2_weight)
        if x == "NICE!":
            player_points += 1
            return render_template("result_right.html", player_points=player_points)
        else:
            temp: int = player_points
            player_points = 0
            return render_template("result_wrong.html", player_points=temp)
    return render_template("game.html", player_one=p1, player_two=p2)



def random_player_name() -> list[str]:
    x: int = randint(1, 400)
    bball_api_response: Response = get(f"https://www.balldontlie.io/api/v1/players/{x}")
    bball_api_response_data = bball_api_response.json()
    player_weight: str = bball_api_response_data['weight_pounds']
    player_name: str = (f"{bball_api_response_data['first_name']} {bball_api_response_data['last_name']}")
    player_info: list[str] = []
    player_info.append(player_name)
    player_info.append(player_weight)
    return player_info









x: int = randint(1, 400)
y: int = randint(1, 400)
bball_api_response: Response = get(f"https://www.balldontlie.io/api/v1/players/{x}")
bball_api_response_two: Response = get(f"https://www.balldontlie.io/api/v1/players/{y}")
#print(bball_api_response.status_code)
bball_api_response_data = bball_api_response.json()
bball_api_response_data_two = bball_api_response_two.json()
#print(bball_api_response_data)


#player_one: str = "Lebron"



if __name__ == '__main__':
    app.run(debug=True)

