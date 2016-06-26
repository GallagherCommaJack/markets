# import numpy as np

def mean(l):
    return sum(l)/len(l)

def bet(bets, wealth, round):

    peoples_true_bets = []
    if 'izaak' in bets:
        peoples_true_bets.append(bets['izaak'][0])
    if 'jack' in bets:
        peoples_true_bets.append(bets['jack'][0])
    if 'tom' in bets:
        peoples_true_bets.append(bets['tom'][0])

    best_bettor = max(wealth, key=wealth.get)
    best_bets = [ bets[best_bettor][0] ]

    good_bets = peoples_true_bets + best_bets

    print "`good_bets`:"
    print good_bets

    if len(good_bets) > 0:
        true_bet = min(
                wealth['andrew'] * .9,
                mean(good_bets)
                )
    else:
        true_bet = 0.0

    false_bet = 0.0

    return true_bet, false_bet

    # If we don't want to accidentally bet on another round without updating
    # our code, we can do something like this:
    #if 0 == round:
    #    return true_bet, false_bet
    #else:
    #    return 0.0, 0.0

