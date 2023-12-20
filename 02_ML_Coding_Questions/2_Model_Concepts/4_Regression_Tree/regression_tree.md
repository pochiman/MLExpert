# Regression Tree

  Create a regression tree to predict the barrels per day (the `bpd`) produced 
  by a particular drilling site, given some `porosity`, `gamma`, `sonic` and 
  `density` values.

  You'll have access to a list of training examples in the `RegressionTree`'s 
  `root` node, specifically in `RegressionTree.root.examples`. Each example is 
  a dictionary with feature keys mapping to their respective values and with a 
  `bpd` key mapping to the example's label.

  Below is an example portion of the `RegressionTree.root.examples`:

[
  {
    "porosity": 0.24230826038076003,
    "gamma": 1.5600463819136288,
    "sonic": 2568.8231147730116,
    "density": -0.353639698833012,
    "bpd": 164.7544334411493, # The label for this example.
  },
  {
    "porosity": 0.4821959432320581,
    "gamma": 1.4953123610344377,
    "sonic": 2768.866560695128,
    "density": 1.1231264377284371,
    "bpd": 157.33821193599536, # The label for this example.
  },
  {
    "porosity": 0.058672948847231135,
    "gamma": 1.5384704880812365,
    "sonic": 3236.794545516582,
    "density": 1.2698807135982118,
    "bpd": 159.49129568528647, # The label for this example.
  },
  # ...  
  # More examples.
]

  Note that:

  • You should use the mean squared error (MSE) as the splitting criteria.
  
  • You shouldn't evaluate `bpd` as a feature to split on, since
    it's what you're trying to predict.

  • You shouldn't use any hyperparameters like max depth.
  
  • There's no need to handle missing data or to scale the features. 

  • Recursive and iterative implementations are both fine.

  • You shouldn't use any libraries that implement regression trees for you,
    such as scikit-learn.
  
  • Your output values will automatically be rounded to the fourth decimal.

  If you're unfamiliar with regression trees, we recommend watching the Decision
  Trees video in the ML Crash Course on MLExpert before starting to code.

# Sample Input

features = {
  "porosity": 0.70,
  "gamma": 1.57,
  "sonic": 3666.90,
  "density": 2.52
}

# Sample Output

143.0698 # The regression tree prediction for the input's bpd.

# Hints

# [Hint_1]

  We first need to train the regression tree. The root node is populated with
  examples, which we need to split up and put into left and right `TreeNode`s. 
  This process can recursively continue to the leaf nodes, at which point there 
  should only be one example left in a node.

# [Hint_2]

  Finding the best split of an example involves evaluating all of its feature
  and split point values to see which split point produces the smallest MSE.
  Each split point value to evaluate is the average of two adjacent feature
  values when the feature values are sorted.

# [Hint_3]

  After finding the split point that minimizes the MSE, an example in a node is
  sent to the left child node if the relevant feature value is less than or
  equal to the split point value. Otherwise, the example is sent to the right
  child node.

# [Hint_4]

  Finding a prediction means traversing down the regression tree while comparing
  the relevant feature values of the input to each node's split point value.

# [Hint_5]

  Upon reaching a leaf node in the regression tree, the prediction is just the
  average of the labels in that leaf node.
