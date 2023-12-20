# Neuron

  Create a single neuron, to be used in a neural network.

  You'll have access to a list `Neuron.examples` of 100 examples,
  where each example is a dictionary with two keys: `"features"` and `"label"`. 
  The value of `"features"` is a list of 3
  features, which have been min-max scaled for you, and the value of `"label"` 
  is `0` or `1`.

  Below is an example portion of the `Neuron.examples`:

[
  {"features": [0.7737498370415932, 0.893981580520576, 0.7776116731845149], "label": 0},
  {"features": [0.8356527294792708, 0.7535044575176968, 0.7940884252881397], "label": 0},
  # ...
  # More examples.
  {"features": [0.25835793676162827, 0.2166447564607853, 0.5066866046843734], "label": 1},
  {"features": [0.34848185391755987, 0.15010261370695727, 0.3466287718524547], "label": 1},
  # ...
  # More examples.
]

  Note that:

  • You shouldn't use regularization.
  
  • You should use mini-batch gradient descent.

  • You should use the sigmoid activation function.
  
  • The neuron should include a weight for the bias and one weight for each
    input feature.

  • You should use `0.01` for the learning rate, 10 examples for the
    mini-batch size, 100 epochs, and the log loss as the loss function. 

  • The `predict` function should return the probability that the
    input should have the label of `1` —not the corresponding `0` or `1` label.

  • Your output value will automatically be rounded to the fourth decimal.

# Sample Input

features = [0.79, 0.89, 0.777]

# Sample Output

0.1636 // The probability that the sample input should have a label of 1.

# Hints

# [Hint_1]

  First, we need to extract mini-batches from the examples. This means
  retrieving a portion of total examples, which will be used to complete one
  iteration of gradient descent.

# [Hint_2]

  Now that we have a mini-batch of examples, we need to get the prediction for
  each example in the mini-batch. This means performing a forward pass through
  the neuron.

# [Hint_3]

  A forward pass for a single example involves multiplying each feature in the
  example by each weight. Don't forget to include a bias in the features, to go
  with the corresponding weight. The bias will just be a `1` appended
  to the features, and the weight for the bias will be treated as just another
  weight. Then, the results of these multiplications are summed up and finally
  passed through a sigmoid to obtain the prediction.

# [Hint_4]

  Sigmoids take the equation: `1/(1 + e^-(x))`. In Python, you'll use
  the `math.exp()` function for `e`.

# [Hint_5]

  After we have the prediction for each example in the mini-batch, we need to
  find the gradient of the loss function with respect to each weight in the
  neuron. The gradient with respect to any weight `i` is the
  difference between the prediction and the true label of an example, multiplied
  by `feature_i`. Since we're using a mini-batch, we sum each
  gradient produced by each example. Finally, we divide each gradient by the
  mini-batch size.

# [Hint_6]

  Now that we have 4 gradients (3 for the inputs and 1 for the bias), we need to
  update the weights as follows:
  `w_i(t+1) = w_i(t) - lr*gradient_i`, where `lr` is the learning rate.

# [Hint_7]

  Now that the weights are updated, we continue through the remaining
  mini-batches until a single epoch is completed; we then repeat the entire
  process for 99 more epochs.

# [Hint_8]

  Now that the neuron is trained, we can get a prediction by performing a
  forward pass with any input features.
