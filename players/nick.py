
def bet(bets, wealth, round):
    trusted = ["abram", "corey", "scott", "evan"]
    base_true = 0.0
    base_false = 0.0
    for person in trusted:
        base_true += bets[person][0]
        base_false += bets[person][1]

    if base_true + base_false == 0.0:
        return 0.0, 0.0

    base_true /= base_true + base_false
    base_false = 1. - base_true

    bet_true = base_true
    bet_false = base_false

    if bet_true > 1:
        bet_true = 0.0
    if bet_false > 1:
        bet_false = 0.0

    my_wealth = wealth['nick']
    bet_true *= 0.40 * my_wealth
    bet_false *= 0.40 * my_wealth

    return bet_true, bet_false
