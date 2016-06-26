def bet(bets,wealth,round):
    # We can get the bets dummy has placed on true and false by querying the bets table
    dummy_true, dummy_false = bets['dummy']
    total_true, total_false = bets['total']

    marketProb = total_true / (total_true + total_false)
    myMoney = wealth['evan']

    myBet = myMoney * 0.5

    # less dummy and total
    nPlayers = len(bets) - 2
    nTrue, nFalse = 0,0
    for player in bets:
        if player == 'dummy' or player == 'total':
            continue
        if bets[player][0] > bets[player][1]:
            nTrue += 1
        else:
            nFalse += 1

##    totalWealth = 0.0
##    for player in wealth:
##        if player == 'dummy' or player == 'total':
##            continue
##        totalWealth += wealth[player]
##
##    weightedBets = {}
##
##    for player in bets:
##        if player == 'dummy' or player == 'total':
##            continue
##        weightedBets[player] = (bets[player][0] * wealth[player] / totalWealth, bets[player][1] * wealth[player] / totalWealth)

    playerRatio = float(nTrue) / float(nFalse)

    if 0 == round:
        # Round 0: "Define p to be marketProb. Question: is 'marketProb > 0.7'"
        if playerRatio >= 0.7:
            return myBet, 0.0
        else:
            return 0.0, myBet
    else:
        return 0.0, 0.0
