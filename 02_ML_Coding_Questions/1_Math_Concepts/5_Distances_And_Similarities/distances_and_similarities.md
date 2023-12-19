# Distance And Similarities

  Write a series of functions that take in two lists, X = x_1 ... x_n and
  Y = y_1 ... y_n and return a list containing:

  • Firstly, the Euclidean distance between X and Y.

  • Secondly, the Manhattan distance between X and Y.

  • Thirdly, the Cosine similarity of X and Y.

  • Finally, the Jaccard similarity of X and Y.

  Note that:

  • You shouldn't use any libraries.

  • Your output values will automatically be rounded to the fourth decimal.

  • X and Y will consist of positive integers up to 1000.

  • X and Y will have cardinalities between 1 and 10 inclusive.

# Sample Input

X = [1, 3, 4, 5]
Y = [7, 6, 3, 1]

# Sample Output

[7.874, 14, 0.6034, 0.3333]

# Hints

# [Hint_1]

  Let’s start by implementing the Metrics class which will calculate all the required
  similarities and distances. We'll start with euclidean_distance. Euclidean distance
  is the rooted sum of squared differences per element in X and Y.

# [Hint_2]

  Next up, the Manhattan distance is the sum of absolute differences per element in X and Y

# [Hint_3]

  Then, we can move on to similarities and begin with cosine similarity. Cosine similarity
  is the normalized dot product between X and Y. The dot product is the sum of the
  element wise multiplication of X and Y. To normalize, we divide the dot product by
  the multiplying together X and Y’s Euclidean norms. The Euclidean norm of a vector is
  the root of the sum of each squared element.

# [Hint_4]

  The final similarity metric to calculate is the Jaccard similarity. This is
  calculated by taking the cardinality of the intersection of X and Y and dividing
  by the cardinality of the union of X and Y.
