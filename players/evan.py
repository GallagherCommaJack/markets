import math

def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']

    marketProb = total_true / (total_true + total_false)
    myMoney = wealth['evan']

    if marketProb > 0.25:
        return 0.0, myMoney * 0.25
    return 0.0, 0.0