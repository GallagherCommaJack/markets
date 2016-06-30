import math

def bet(bets, wealth, rnd):
    total_true, total_false = bets['total']
    prob = total_true / (total_true + total_false)

    if prob > 0.7:
        return 30.0, 0.0
    else:
        return 0.0, 30.0

