def bet(bets,wealth,round):

    # wealth-weighted average bot

    # max_bet = 0.7
    weighted_true = 0
    weighted_false = 0
    my_wealth = wealth["daniel"]

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

    return 0.8 * my_wealth * tratio, 0.8 * my_wealth * fratio
