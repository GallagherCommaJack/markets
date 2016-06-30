import math

def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']

    # today's DOW
    # 17,409.72
    # so very likely number like
    #   xxx-x(3-6)71

    marketProb = total_true / (total_true + total_false)
    myMoney = wealth['evan']

    myEstProb = 0.20

    if marketProb > myEstProb:
        return 0.0, min(myMoney * 0.5, (marketProb - myEstProb) * myMoney)
    return 0.0, 0.0