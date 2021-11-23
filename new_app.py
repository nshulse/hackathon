from flask import Flask, render_template, request
from requests import get  # This function is how we will make requests to a server.
from requests.models import Response  # This is the type of a Response object.
from random import randint
from helpers import check_answer


tester: int


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

#Problem: Sometimes player does not have recorded stats for some categories.
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



def what_question() -> None:
    global big_question, p1_weight, p2_weight
    tester: int = randint(1, 8)
    print(tester)
    if tester == 1:
        big_question = "WHO SCORES THE MOST POINTS"
        p1_weight = player_one.stats['pts']
        p2_weight = player_two.stats['pts']
    elif tester == 2:
        big_question = "WHO MAKES THE MOST THREES"
        p1_weight = player_one.stats['fg3m']
        p2_weight = player_two.stats['fg3m']
    elif tester == 3:
        big_question = "WHO GETS THE MOST REBOUNDS"
        p1_weight = player_one.stats['reb']
        p2_weight = player_two.stats['reb']
    elif tester == 4:
        big_question = "WHO GETS THE MOST ASSISTS"
        p1_weight = player_one.stats['ast']
        p2_weight = player_two.stats['ast']
    elif tester == 5:
        big_question = "WHO GETS THE MOST TURNOVERS"
        p1_weight = player_one.stats['turnover']
        p2_weight = player_two.stats['turnover']
    elif tester == 6:
        big_question = "WHO HAS THE HIGHEST FILED GOAL PERCENTAGE"
        p1_weight = player_one.stats['fg_pct']
        p2_weight = player_two.stats['fg_pct']
    elif tester == 7:
        big_question = "WHO HAS THE HIGHEST THREE POINT PERCENTAGE"
        p1_weight = player_one.stats['fg3_pct']
        p2_weight = player_two.stats['fg3_pct']
    elif tester == 8:
        big_question = "WHO WEIGHS MORE"
        p1_weight = player_one.weight
        p2_weight = player_two.weight
    else:
        big_question = "wtff"
        p1_weight = player_one.weight
        p2_weight = player_two.weight
        print("errorororor")



#player_one = get_player()
#player_two = get_player()

player_one: Player
player_two: Player

app: Flask = Flask(__name__)



p1 = 0
p2 = 1
player_points = 0
p1_weight = 0
p2_weight = 0
x: int = 0

@app.route("/")
def index():
    return render_template('index.html')

"""@app.route('/game', methods=["GET", "POST"])
def game():
    global p1, p2, player_points, p1_weight, p2_weight
    if request.method == "GET":
        player_one_list = random_player_name()
        player_two_list = random_player_name()
        p1 = player_one_list[0]
        p1_weight = player_one_list[1]
        p2 = player_two_list[0]
        p2_weight = player_two_list[1]
        #player_points: int = 0
        while p1_weight == None:
            p1 = random_player_name()
        while p2_weight == None:
            p2 = random_player_name()
        while p2_weight == p1_weight:
            p2 = random_player_name()
        p1_weight = int(p1_weight)
        p2_weight = int(p2_weight)
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
    return render_template("game.html", player_one=p1, player_two=p2)"""



"""def random_player_averages() -> None:
    cat: int
    cat = randint(1, 8)
    print(cat)
    if cat == 1:
        tester = 'pts'
        #return player_one.stats['pts']
    if cat == 2:
        tester = 'fg3m'
        #return player_one.stats['fg3m']
    if cat == 3:
        tester = 'reb'
        #return player_one.stats['reb']
    if cat == 4:
        tester = 'ast'
        #return player_one.stats['ast']
    if cat == 5:
        tester = 'turnover'
        #return player_one.stats['turnover']
    if cat == 6:
        tester = 'fg_pct'
        #return player_one.stats['fg_pct']
    if cat == 7:
        tester = 'fg3_pct'
        #return player_one.stats['fg3_pct']
    if cat == 8:
        tester = 'weight'
        #return player_one.weight
    else:
        tester ='error'"""



"""def what_question() -> None:
    global tester, big_question, p1_weight, p2_weight
    tester = randint(1, 8)
    if tester == 1:
        big_question = "WHO SCORES THE MOST POINTS"
        p1_weight = player_one.stats['pts']
        p2_weight = player_two.stats['pts']
    if tester == 2:
        big_question = "WHO MAKES THE MOST THREES"
        p1_weight = player_one.stats['fg3m']
        p2_weight = player_two.stats['fg3m']
    if tester == 3:
        big_question = "WHO GETS THE MOST REBOUNDS"
        p1_weight = player_one.stats['reb']
        p2_weight = player_two.stats['reb']
    if tester == 4:
        big_question = "WHO GETS THE MOST ASSISTS"
        p1_weight = player_one.stats['ast']
        p2_weight = player_two.stats['ast']
    if tester == 5:
        big_question = "WHO GETS THE MOST TURNOVERS"
        p1_weight = player_one.stats['turnover']
        p2_weight = player_two.stats['turnover']
    if tester == 6:
        big_question = "WHO HAS THE HIGHEST FILED GOAL PERCENTAGE"
        p1_weight = player_one.stats['fg_pct']
        p2_weight = player_two.stats['fg_pct']
    if tester == 7:
        big_question = "WHO HAS THE HIGHEST THREE POINT PERCENTAGE"
        p1_weight = player_one.stats['fg3_pct']
        p2_weight = player_two.stats['fg3_pct']
    if tester == 8:
        big_question = "WHO WEIGHS MORE"
        p1_weight = player_one.weight
        p2_weight = player_two.weight
    else:
        big_question = "wtff"
        p1_weight = player_one.weight
        p2_weight = player_two.weight
        print("errorororor")"""


#x: int = randint(1, 400)
#y: int = randint(1, 400)
#bball_api_response: Response = get(f"https://www.balldontlie.io/api/v1/players/{x}")
#bball_api_response_two: Response = get(f"https://www.balldontlie.io/api/v1/players/{y}")
#print(bball_api_response.status_code)
#bball_api_response_data = bball_api_response.json()
#bball_api_response_data_two = bball_api_response_two.json()
#print(bball_api_response_data)


#bball_averages_response: Response = get("https://www.balldontlie.io/api/v1/season_averages?player_ids[]=237")
#bball_averages_data = bball_averages_response.json()



#player_one: str = "Lebron"




# 1. Starting small
# Endpoint: https://boredapi.com/api/activity/, returns a random activity for you to do.

#bored_api_response: Response = get("https://boredapi.com/api/activity/")
#print(bored_api_response.status_code)
# 200 nice

#bored_api_response_data = bored_api_response.json()
#print(bored_api_response_data)
# 2. Requests with params
# Endpoint: https://api.agify.io, returns average age for people with a given name (passed as a parameter)

#agify_api_response: Response = get("https://api.agify.io", params={"name": ""})
#print(agify_api_response.status_code)
#agify_api_response_data = agify_api_response.json()
#print(agify_api_response_data)

#def grab_url(planet: str, is_planet: bool) -> str:
    #"""Helper function to populate url variable in app.py. The file paths we build relate to files in our 'static' directory."""
    #if is_planet:
        #return f"/{planet.lower()}.jpg"
    #else:
        #return f"/space.jpg"

# 3. Requests with an API key
# TODO: Sign up for an API key: https://api.nasa.gov/
# Endpoint: https://api.nasa.gov/planetary/apod, returns the astronomy picture of the day! 

#apod_response: Response = get("https://api.nasa.gov/planetary/apod?", params={"api_key": "n5RpwOp1rWmPRkndpYbAsD9IiZcahcMQuWRDPtzP"})
#print(apod_response.status_code)
#print(apod_response.json())


#bball_api_response: Response = get("https://www.balldontlie.io/api/v1/players/6")
#print(bball_api_response.status_code)
#bball_api_response_data = bball_api_response.json()
#print(bball_api_response_data)


@app.route('/game', methods=["GET", "POST"])
def game():
    global player_points, big_question, player_one, player_two
    player_one = get_player()
    player_two = get_player()
    what_question()
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
    return render_template("new_game.html", player_one=player_one.name, player_two=player_two.name, question=big_question)




if __name__ == '__main__':
    app.run(debug=True)


