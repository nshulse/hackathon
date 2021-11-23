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