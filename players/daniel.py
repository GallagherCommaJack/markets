def bet(bets,wealth,round):

    # wealth-weighted average bot
    
    weighted_true = 0
    weighted_false = 0

    for player in bets.items():
        name = player[0]
        if name == "total" or name == "daniel":
            continue
        bet_true = player[1][0]
        bet_false = player[1][1]

        weighted_true += bet_true * wealth[name]
        weighted_false += bet_false * wealth[name]

    weighted_total = weighted_true + weighted_false
    tratio = weighted_true/weighted_total
    fratio = weighted_false/weighted_total

    if abs(weighted_true - weighted_false) < 0.01:
        return 0.0, 0.0

    if weighted_true > weighted_false:
        if tratio < 0.9:
            return tratio * wealth["daniel"], 0.0
        else:
            return 0.9 * wealth["daniel"], 0.0
    else:
        if fratio < 0.9:
            return 0.0, fratio * wealth["daniel"]
        else:
            return 0.0, 0.9 * wealth["daniel"]
