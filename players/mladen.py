import math

current_rnd = 0
cap_factor = 0.6

def bet(bets, wealth, rnd):
    total_true, total_false = bets['total']
    prob = total_true / (total_true + total_false)
    
    my_wealth = wealth['mladen']
    wealth = cap_factor * my_wealth

    true_fac = min(math.exp(100 * (prob - 0.7)) / math.exp(100 * 0.3), 1)
    false_fac = 1 - true_fac
    
    true_money = true_fac * wealth
    false_money = false_fac * wealth

    # If we don't want to accidentally bet on another round without updating our code, we can do something like this:
    if rnd == current_rnd:
        return true_money, false_money
    else:
        return 0.0, 0.0

