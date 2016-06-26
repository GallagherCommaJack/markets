def bet(bets,wealth,round):
    total_true, total_false = bets["total"]
    p = total_true /(total_true + total_false)
    me = "william"
    my_true, my_false = bets[me]

    my_wealth = wealth[me]

    if round == 0:
        bet_size = my_wealth
        epsilon = 0.05
        if p > 0.7 + epsilon:
            return bet_size, 0.0
        if p < 0.7 - epsilon:
            return 0.0, bet_size
        my_true = max(((p - 0.7) / epsilon) * bet_size, 0)
        return my_true, bet_size - my_true
    else:
        return 0.0, 0.0 #true, false

if __name__ == "__main__":
    bets = {"william":(0.0,0.0),"dummy":(10.0,10.0),"total":(10.0,10.0)}
    wealth = {"william":100.0,"dummy":20.0,"total":20.0}
    round = 0
    print bet(bets,wealth,round)