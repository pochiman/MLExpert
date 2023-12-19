# Repeating Heads

  You’re considering a $100 bet with your friend. If `n`  consecutive
  fair coin flips result in all heads, then you win - else your friend wins. 
  Your friend agrees to let you attempt the bet as many times as you’d like. 
  Assuming you attempt the bet `x` times, what's the probability that you’ll 
  win the bet at least once? As well, what should your winning payout ($100, 
  $200, etc) be to ensure that you at least break even given unlimited 
  attempts of the bet?

  Write a function which takes in the number of consecutive coin flips (n) 
  and the number of bet attempts (x) and returns a list containing:

  • Firstly, the probability that you win the bet at least once

  • Secondly, your required winning payout

  Note that:

  • You can assume a fair coin.

  • You shouldn't use any libraries.

  • Your output values will automatically be rounded to the fourth decimal.
  
# Sample Input

n = 3
x = 10

# Sample Output

[73.6…, 135.6…]

# Hints

# [Hint_1]

  First, we need to identify the chance of flipping a heads on a fair coin. 
  It’s 50%

# [Hint_2]

  Then, we need to determine the chance of flipping n heads in a row - this is 
  referred to as a trial. That’s going to be the chance of flipping heads a 
  single time raised to the power of n.

# [Hint_3]

  Then, we need to establish what the chance of us losing a single trial is.
  This is 1 - the chance of a single winning trial
  
# [Hint_4]

  Next, we need to know the chance of losing n consecutive trials.
  This is going to be the chance of losing a single trial raised to the
  power of the number of bet attempts. We can subtract this result from
  1 to obtain the probability that we’ll win the bet given a number of 
  attempts.

# [Hint_5]

  Finally, we can determine the winning payout required to break even given
  infinite attempts. We do this by multiplying the chance of winning by an
  unknown payout size and setting the equation equal to the original bet size.
  Solving for the unknown payout results in the required winning payout.
