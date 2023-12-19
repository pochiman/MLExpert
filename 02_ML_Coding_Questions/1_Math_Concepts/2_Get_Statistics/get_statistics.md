# Get Statistics

  Write a function that takes in a list of numbers and returns a dictionary
  containing the following statistics about the numbers: the mean, median, mode,
  sample variance, sample standard deviation, and 95% confidence interval for
  the mean.

  Note that:

  • You can assume that the given list contains a large-enough number of samples
    from a population to use a z-score of `1.96`.

  • If there's more than one mode, your function can return any of them.

  • You shouldn't use any libraries.

  • Your output values will automatically be rounded to the fourth decimal.
  
# Sample Input

input_list = [2, 1, 3, 4, 4, 5, 6, 7]

# Sample Output

{
  "mean": 4.0,
  "median": 4.0,
  "mode": 4.0,
  "sample_variance": 4.0,
  "sample_standard_deviation": 2.0,
  "mean_confidence_interval": [2.6141, 5.3859],
}

# Hints

# [Hint_1]

  The mean is the sum of the values divided by the number of values.

# [Hint_2]

  The median is the middle value of the sorted values. If the input list has an
  even number of elements, the median is the average of the two middle values.
  
  Naturally, you'll first have to sort the input list, and you'll then have to
  find the middle index (or the two middle indices if the list has an even
  number of elements).

# [Hint_3]

  The mode is the most frequent element in the input list.
  You'll have to count how many times each value appears in the list.
  
# [Hint_4]

  What's the difference between a sample variance and a population variance?

# [Hint_5]
  
  The variance of a sample is the sum of the squared differences between each
  element and the mean of the elements. Each term in the sum is divided by the
  number of input elements minus 1.

# [Hint_6]

  The sample standard deviation is the square root of the sample variance.

# [Hint_7]

  To find the 95% confidence interval of the mean, you first need to find the
  z-score of 95%, which is `1.96` assuming a two-tailed distribution.

  This `1.96` is then multiplied by the standard error, which is the standard 
  deviation divided by the square root of the number of input elements.

  Finally, the lower end of the confidence interval is obtained by subtracting 
  `1.96 * standard_error` from the mean, and the upper end is obtained by adding 
  `1.96 * standard_error` to the mean.
