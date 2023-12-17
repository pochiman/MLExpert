# 9 - Logistic Regression

Where linear regression is used to predict outputs that can take on an infinite 
number of values, logistic regression instead aims to solve problems where the 
number of outcomes are limited.

And much like its cousin, this supervised-learning technique boasts a high level 
of popularity in machine-learning circles.

# Key Terms

# [Sigmoid_Function]
Also the logistic function, a function which outputs a range from 0 to 1.

# [Closed-Form_Solution] π
For our case, this is what ordinary least squares provides for linear regression. 
It's a formula which solves an equation.

# [Cross-Entropy_Loss]
A loss function which is used in classification tasks. It's technically the entropy 
of the true labels plus the KL-divergence of the predicted and true labels. Minimizing 
the cross-entropy minimizes the difference between the true and predicted label 
distributions.

# [Parameters]
Also, weights, or coefficients. Values to be learned during the model training.

# [Learning_Rate]
A multiple, typically less than 1, used during the parameter update step during 
model training to smooth the learning process.

# [Odds_Ratio] π
The degree of associate between two events. If the odds ratio is 1, then the two 
events are independent. If the odds ratio is greater than 1, the events are 
positively correlated, otherwise the events are negatively correlated.

# [Multinomial_Logistic_Regression]
Logistic Regression in which there are more than two classes to be predicted across.

# [Softmax]
A sigmoid which is generalized to more than two classes to be predicted against.

# [Gradient_Descent]
An iterative algorithm with the goal of optimizing some parameters of a given 
function with respect to some loss function. If done in batches, all of the examples 
are considered for an iteration of gradient descent. In mini-batch gradient descent, 
a subset of examples are considered for a single iteration. Stochastic gradient 
descent considers a single example per gradient descent iteration.

# [Downsampling]
Removing a number of majority class examples. Typically done in addition to upweighting.

# [Upweighting]
Increasing the impact a minority class example has on the loss function. Typically 
done in addition to downsampling.

# [Epoch]
One complete cycle of training on all of the examples.

# [Regularization]
A technique of limiting the ability for a model to overfit by encouraging the values 
parameters to take on smaller values.

# [Early_Stopping]
Halting the gradient descent process prior to approaching a minima or maxima.

# [Mcfadden's_Pseudo_R-squared] π
An analog to linear regression's R-squared which typically takes on smaller values 
than the traditional R-squared.

# [Generative_Model]
A model which aims to approximate the joint probability of the features and labels.

# [Discriminative_Model]
A model which aims to approximate the conditional probability of the features and 
labels.
