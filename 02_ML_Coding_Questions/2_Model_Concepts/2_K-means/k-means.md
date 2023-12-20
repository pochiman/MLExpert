# K-means

  Use the k-means algorithm to return the `k` means (or centroids)
  for the provided user features.

  These user features are the result of a dimensionality reduction by PCA on
  some user-app interaction data. You'll have access to a `USER_FEATURE_MAP` 
  dictionary, mapping each user `"uid_i"` to a respective list of 4 features 
  associated with the user in question.

  Below is an example portion of the `USER_FEATURE_MAP`:

{
  "uid_0": [-1.479359467505669, -1.895497044385029, -2.0461402601759096, -1.7109256402185178],
  "uid_1": [-1.8284426855307128, -1.714098142408679, -0.9893682669649455, -1.5766569391907947],
  "uid_2": [-1.8398933218386004, -1.7896757009107565, -1.1370177175666063, -1.0218512556903283],
  "uid_3": [-1.23224975874512, -1.8447858273094768, -1.8496517744301924, -2.4720755654344186],
  "uid_4": [-1.7714737791268318, -1.2725603446513774, -1.5512094954034525, -1.2589442628984848],
  # ...
  # More of the same kind of data.
}

  Note that:

  • The initial centroid locations are selected for you to ensure consistency
    when verifying your solution.

  • You should execute at least 10 iterations of the k-means algorithm, not
    including the initialization of the centroids.

  • You should use the Manhattan distance as the distance metric.
  
  • You shouldn't use any libraries that implement k-means for you. 

  • Your output values will automatically be rounded to the fourth decimal.

  If you're unfamiliar with the k-means algorithm, we recommend watching the
  k-means video in the ML Crash Course on MLExpert before starting to code.

# Sample Input

k = 1

# Sample Output

[[-1.066, -1.098, -1.067, -1.085]]
# The location of the 1 mean (centroid) in 4-dimensional space.

# Hints

# [Hint_1]

  Start by creating `k` centroids based on the locations of the provided users.

# [Hint_2]

  After creating the centroids, find the nearest centroid for each point, and
  assign each point to its nearest centroid.


# [Hint_3]

  After finding each point's nearest centroid, update the location of each
  centroid to be the average of each point assigned to it. Calculating the
  average of n-dimensional data is the same as calculating the average of
  one-dimensional data; you just handle each dimension separately.

# [Hint_4]

  Repeat the entire process of updating the centroids at least 10 times to allow
  for the centroids to converge on the means of the features.
