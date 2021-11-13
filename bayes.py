

prior = 0.01 #prevalence if no other indicators
#sensitivity to get a positive result on an infected person
sensitivity = 0.9
#FNR false negative rate (negative result on infected person)
FNR = 1-sensitivity
#get a negative result on a non-infected person
specificity = 0.91
#FPR false positive rate (positive on non-infected)
FPR = 1-specificity

#bayes factor for positive test outcome
def bayes_factor_pos(sensitivity, FPR) -> float:
    """ Returns the Bayes factor = P(+|infected)/P(+|non-infected) """

    return sensitivity/FPR

#bayes factor for negative test outcome
def bayes_factor_neg(FNR, specificity) -> float:
    """ Returns the Bayes factor  = P(-|infected)/P(-|non-infected) """

    return FNR/specificity

def translate_prior_to_odds(prior):
    """ Returns the 1 to x ratio """
    # return 1 out of x
    return 1/prior-1

if __name__ == '__main__':
    bayes = bayes_factor_pos(sensitivity, FPR)
    prior_as_odds = translate_prior_to_odds(prior)
    probability_of_being_infected = bayes/(prior_as_odds + bayes)
    print(f"probability of an infection with a positive test: " \
          f"{round(probability_of_being_infected*100, 2)}%")
    bayes2 = bayes_factor_neg(FNR, specificity)
    probability_of_being_infected2 = bayes2/(translate_prior_to_odds(prior) + bayes2)
    print(f"probability of an infection with a negative test: " \
          f"{round(probability_of_being_infected2*100, 2)}%")