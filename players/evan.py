import math

def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']

    marketProb = total_true / (total_true + total_false)
    myMoney = wealth['evan']

    myBet = myMoney * 0.5

    # less dummy and total
    nPlayers = len(bets) - 2
    nTrue, nFalse = 1,1
    for player in bets:
        if player == 'dummy' or player == 'total':
            continue
        if bets[player][0] > bets[player][1]:
            nTrue += 1
        else:
            nFalse += 1

    totalWealth = 0.0
    for player in wealth:
        if player == 'dummy' or player == 'total':
            continue
        totalWealth += wealth[player]

    weightedBets = {}
    playerProb = {}
    reasonableBets = []

    # Round 0: log_10 (Population of Brazil) / 10 > rand[0,1]
    myBestGuess = math.log10(5.0 * 10.0**8) / 10
    crazyLow = math.log10(1.0 * 10.0**7) / 10
    crazyHigh = math.log10(1.0 * 10.0**9) / 10

    riskiness = dict([(p, '0.5') for p in bets])

    for player in bets:
        if player == 'dummy' or player == 'total' or wealth[player] == 0.0 or sum(bets[player]) == 0.0:
            continue
        weightedBets[player] = (bets[player][0] * wealth[player] / totalWealth, bets[player][1] * wealth[player] / totalWealth)

        if bets[player][0] > 0.0 and bets[player][1] > 0.0:
            playerProb[player] = (bets[player][0] / (bets[player][0] + bets[player][1]))
            if playerProb[player] >= crazyLow and playerProb[player] <= crazyHigh:
                reasonableBets.append(playerProb[player])

        # heuristic--are they too confident (somehow) relative to their wealth? (whatever that means)
        # actually this needs to depend on the market prob more directly
        else:
            # market is too low, are they strong on no?
            if marketProb < myBestGuess:
                playerProb[player] = 1 - bets[player][1] / wealth[player]
            else: # market too high, are they strong on yes?
                playerProb[player] = bets[player][0] / wealth[player]

            if playerProb[player] >= crazyLow and playerProb[player] <= crazyHigh:
                reasonableBets.append(playerProb[player])

    playerRatio = float(nTrue) / float(nFalse)

    reasonableMarketGuess = myBestGuess
    if len(reasonableBets) > 0:
        reasonableMarketGuess = sum(reasonableBets) / len(reasonableBets)
    myAdjustedProb = (myBestGuess + reasonableMarketGuess) / 2.0

    # if more time: throw out crazy bets
    myAdjustedProb = myBestGuess

    if marketProb < myAdjustedProb:
        return myBet, 0.0
    return 0.0, myBet

##    if 0 == round:
##        # Round -1: "Define p to be marketProb. Question: is 'marketProb > 0.7'"
##        if playerRatio >= 0.7:
##            return myBet, 0.0
##        else:
##            return 0.0, myBet
##    else:
##        return 0.0, 0.0
