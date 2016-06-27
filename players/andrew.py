def meeen(l):
    return sum(l) / float(len(l))

def bet(bets, wealth, round):

    peoples_true_bet_proportions = []
    if 'izaak' in bets:
        peoples_true_bet_proportions.append(
                bets['izaak'][0] / wealth['izaak'])
    if 'jack' in bets:
        peoples_true_bet_proportions.append(
                bets['jack'][0] / wealth['jack'])
    if 'tom' in bets:
        peoples_true_bet_proportions.append(
                bets['tom'][0] / wealth['tom'])

    best_bettor = max(wealth, key=wealth.get)
    best_true_bet_proportions = [ bets[best_bettor][0] / wealth[best_bettor] ]

    good_true_bet_proportions = (peoples_true_bet_proportions +
            best_true_bet_proportions)

    if len(good_true_bet_proportions) > 0:
        true_bet = min(
                wealth['andrew'] * .9,
                wealth['andrew'] * meeen(good_true_bet_proportions)
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

