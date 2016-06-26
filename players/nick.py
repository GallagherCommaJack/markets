CURRENT_ROUND = 0


def bet(bets, wealth, round):
    if CURRENT_ROUND != round:
        return 0.0, 0.0

    # We can get the bets dummy has placed on true and false by querying the bets table
    # tot_true = 0
    # tot_false = 0
    # for bet_true, bet_false in bets.items():
    #     tot_true += bet_true
    #     tot_false += tot_false
    #
    # avg_true = tot_true / len(bets.items())
    # avg_false = tot_false / len(bets.items())

    total_true, total_false = bets["total"]

    if (total_true/(total_true + total_false)) > 0.7:
        bet_true = 0.5
        bet_false = 0.0
    else:
        bet_true = 0.0
        bet_false = 0.5

    # We can also see how much wealth a player has by querying wealth
    my_wealth = wealth['nick']

    bet_true *= 0.25 * my_wealth
    bet_false *= 0.25 * my_wealth

    return bet_true, bet_false
