# Probability Of Disease

  A test indicating the presence of disease in cats is 95% accurate in terms of
  both sensitivity and specificity. The prevalence of the disease is 3% which means
  only 3% of known cats have the disease. If your cat tests positive (negative)
  for the disease, what’s the probability that your cat has (doesn’t have) the disease?

  Write a program which takes in the accuracy of a test as well as the percent of
  a population which has the disease and returns a list containing:

  • Firstly, the probability that an individual has the disease given a positive 
    test result.

  • Secondly, the probability that an individual does not have the disease given 
    a negative test result.

  Note that:

  • You can assume the sensitivity and specificity are equal to the accuracy

  • You shouldn't use any libraries.

  • Your output values will automatically be rounded to the fourth decimal.
  
# Sample Input

accuracy = .95
prevalence = .03

# Sample Output

[73.6…, 135.6…]

# Hints

# [Hint_1]

  First, the probability of any random person having the disease is the prevalence.
  The chance of a person not having the disease is 1 - prevalence. As well,
  the inaccuracy of the test is 1 - accuracy. Keep in mind the accuracy here
  is equal to both the sensitivity and specificity.

# [Hint_2]

  Second, we need to determine the probability of testing positive.
  We do that by adding together the probability of being sick and the test being accurate
  plus the probability of being healthy and the test being inaccurate. This calculation
  will be our denominator in figuring out the prob_healthy_given_negative.

# [Hint_3]

  To figure out the prob_healthy_given_negative we put the probability of testing
  negative in the case of being healthy and divide by the calculation in the previous hint.
  
# [Hint_4]

  Finally, we need to determine prob_sick_given_positive. We do a similar calculation as
  the previous hint but this time the numerator will be the probability of testing
  positive in the case of being sick. The denominator will be the probability of
  testing positive in the case of being sick plus the probability of testing positive
  in the case of being healthy. This denominator covers all the ways a positive test can arise.
