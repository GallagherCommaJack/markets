

def bet(bets, wealth, round):
  total_true, total_false = bets['total']
  p_true = total_true / (total_true + total_false)
  proportion = 0.3
  my_wealth = wealth['jessica'] * proportion
  def standard_bet(prob):
    return (prob * my_wealth, (1 - prob) * my_wealth)
  if round == 0:
    # p > 0.7
    if p_true > 0.701:
      my_prob = 1.0
    elif p_true < 0.699:
      my_prob = 0.0
    else:
      my_prob = 0.5
    return standard_bet(my_prob)
  else:
    return 0.0, 0.0



