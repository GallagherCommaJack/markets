# name = __name__.split('.')[-1]

def bet(bets, wealth, round):
    # That p > .7
    t, f = bets['total']
    p = t / (t + f)
    
    if p > .7:
        10.0, 0.0
    else:
        return 0.0, 10.0
