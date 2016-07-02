import math

def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']
    marketProb = total_true / (total_true + total_false)
    myWealth = wealth['evan']
##
##    # today's DOW
##    # 17,409.72
##    # so very likely number like
##    #   xxx-x(3-6)71
##
##
##
##    myEstProb = 0.20
##
##    if marketProb > myEstProb:
##        return 0.0, min(myMoney * 0.5, (marketProb - myEstProb) * myMoney)
##    return 0.0, 0.0
##
##    myBet = myMoney * 0.5
##
##    # less dummy and total
    nPlayers = len(bets) - 2
    nTrue, nFalse = 1,1
    for player in bets:
        if player == 'dummy' or player == 'total':
            continue
        if bets[player][0] > bets[player][1]:
            nTrue += 1
        else:
            nFalse += 1

    if marketProb > 0.8:
        return 0.00, myWealth * (marketProb - 0.8) * (0.5 / 0.2)
    if marketProb < 0.2:
        return myWealth * (0.2 - marketProb) * (0.5 / 0.2), 0.00

    if marketProb > 0.4 and marketProb < 0.6:
        if nTrue > nFalse:
            return myWealth * marketProb, 0.00
        else:
            return 0.00, myWealth * marketProb

    return 0.0, 0.0