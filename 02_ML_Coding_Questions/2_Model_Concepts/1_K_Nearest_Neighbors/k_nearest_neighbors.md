# K Nearest Neighbors

  Use the k-nearest neighbors algorithm to return the `k` nearest
  neighbors of the provided features.

  These features are the result of a dimensionality reduction by PCA on some
  operating-system data related to processes and their intrusivity in some
  network. You'll have access to an `EXAMPLES` dictionary, mapping
  each process identifier `"pid_i"` to a respective dictionary
  containing its associated features as well as a label representing whether the
  relevant process was intrusive to the network. A label of `0` means
  that it wasn't intrusive, while a label of `1` means that it was intrusive.

  Below is an example portion of the `EXAMPLES`:

{
  "pid_0": {
    "features": [3.968642003034218, 3.9553899901567955, 3.8067717105202794, # ... more words],
    "is_intrusive": 0,
  }, 
  "pid_1": {
    "features": [3.905930716908446, 3.9843869514613046, 3.999386668299634, # ... more words],
    "is_intrusive": 0,
  }, 
  # ...
  # More of the same kind of data.
  "pid_500": {
    "features": [4.309361217767318, 4.287392829732823, 4.296809382863873, # ... more words],
    "is_intrusive": 1,
  },
  "pid_501": {
    "features": [4.310938448487633, 4.298506635010131, 4.256964230013101, # ... more words],
    "is_intrusive": 1,
  },
  # ...
  # More of the same kind of data.
}

  Note that:

  • You should use the Euclidean distance as the distance metric when finding
    the k-nearest-neighbors.

  • You shouldn't use any libraries that implement KNN for you.

  If you're unfamiliar with the k-nearest neighbors algorithm, we recommend
  watching the K Nearest Neighbors video in the ML Crash Course on MLExpert
  before starting to code.

# Sample Input

# For the `find_k_nearest_neighbors` function.
features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
k = 1

# Sample Output

["pid_535"]
# The closest neighbor to the input features.
# Only 1 neighbor is returned since k = 1.

# Sample Input

# For the `predict_label` function.
features = [4.30936122, 4.28739283, 4.29680938, 4.33571647, 4.28774593]
k = 1

# Sample Output

1
# The predicted label of the input features based on the closest neighbor.

# Hints

# [Hint_1]

  To implement `find_k_nearest_neighbors`, we need to iterate through
  all the features in our data set and find the distances between each feature
  and each of the features provided to `find_k_nearest_neighbors`. 

# [Hint_2]

  By distance, we mean Euclidean distance. To find the Euclidean distance
  between two features, we start by iterating through each element in both
  features, subtracting one value from the other, and squaring that result. We
  now have a list of squared differences, one for each item in the features. We
  can get the Euclidean distance by summing each element in the list and taking
  the square root.

# [Hint_3]

  After we have the Euclidean distances between each feature in our data set and
  each of the provided features, we can sort these distances and take the top k
  elements so as to obtain the k-nearest neighbors.

# [Hint_4]

  We can now use `find_k_nearest_neighbors` to implement `predict_label`. We 
  only need to get the labels of the k nearest neighbors and return the most 
  popular one among them; this is the prediction.
