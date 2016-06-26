import math


def bet(bets, wealth, round):
    pop_brazil = 50000000
    encoded_brazil = math.log10(pop_brazil)/10.0

    total_true, total_false = bets["total"]
    market_prediction = total_true / (total_true + total_false)
    adjustment = 0.25 * (market_prediction - encoded_brazil)
    bet_true = encoded_brazil + adjustment
    bet_false = 0.0

    # We can also see how much wealth a player has by querying wealth
    my_wealth = wealth['nick']

    bet_true *= 0.25 * my_wealth
    bet_false *= 0.25 * my_wealth

    return bet_true, bet_false
