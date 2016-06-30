def bet(bets,wealth,round):
    total_true, total_false = bets["total"]
    p = total_true /(total_true + total_false)
    me = "william"
    my_true, my_false = bets[me]
    my_wealth = wealth[me]

    wealths = [(k, v) for (k,v) in wealth.items() if k not in ["total","dummy",me]]
    wealths = sorted(wealths, key = lambda x: x[1])
    best_players = [k for (k, v) in wealths[:2]]

    bet_size = my_wealth / 2.0
    pos = 0.0
    neg = 0.0
    for name in best_players:
        pos +=  bets[name][0]
        neg +=  bets[name][1]
    x = pos + neg
    if pos + neg > 0.0:
        pos *= (bet_size / x)
        neg *= (bet_size / x)
    return pos, neg

if __name__ == "__main__":
    for i in range(20):
        bets = {"william":(0.0,0.0),"joe":(float(i),20.0-i),"joe2":(20.0,0),"total":(float(i),20.0-i)}
        wealth = {"william":100.0,"joe":20.0,"joe2":20.0,"total":20.0}
        round = 0
        print float(i)/20.0, bet(bets,wealth,round)