def bet(bets,wealth,round):
    total_true, total_false = bets["total"]
    p = total_true /(total_true + total_false)
    me = "william"
    my_true, my_false = bets[me]
    my_wealth = wealth[me]

    num_pos = 0
    num_neg = 0
    for name, bet in bets.items():
        if name not in ["total","dummy"] and not (bet[0] == 0.0 and bet[1] == 0.0):
            pos = bet[0] / p
            neg = bet[1] / p
            if pos > neg:
                num_pos += 1
            else:
                num_neg += 1
    if num_pos > num_neg:
        return 0.0, 0.0
    else:
        return 0.1, 0.0
    # bet_size = my_wealth / 5.0
    # epsilon = 0.001
    # my_p = 0.8
    # if my_p > p:
    #     return min((my_p - p) / epsilon, 1) * bet_size, 0
    # else:
    #     return 0, min((p - my_p) / epsilon, 1) * bet_size

if __name__ == "__main__":
    for i in range(20):
        bets = {"william":(0.0,0.0),"dummy":(float(i),20.0-i),"total":(float(i),20.0-i)}
        wealth = {"william":100.0,"dummy":20.0,"total":20.0}
        round = 0
        print float(i)/20.0, bet(bets,wealth,round)