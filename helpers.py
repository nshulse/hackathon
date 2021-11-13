def check_answer(player: str, p1: int, p2: int) -> str:
    #if player == "one" and p1 > p2:
        #return "NICE!"
    #if player == "two" and p2 > p1:
        #return "NICE!"
    global player_points
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
