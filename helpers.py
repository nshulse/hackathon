from typing import Union
from random import randint

def check_answer(player: str, p1: Union[float, int, None], p2: Union[float, int, None]) -> str:
    
    #if player == "one" and p1 > p2:
        #return "NICE!"
    #if player == "two" and p2 > p1:
        #return "NICE!"
    global player_points

    #if isinstance(p1, int):

    if player == "one":
        if p1 > p2:
            return "NICE!"
        else:
            player_points = 0
            return "L"
    if player == "two":
        if p1 > p2:
            player_points = 0
            return "L"
        else:
            return "NICE!"
