# Deep Learning

# 13 - Neural Networks

You might be thinking that artificial neural networks are this scary, complex 
topic. And you'd be absolutely correct.

Fortunately, you're equipped with the most powerful neural network of them all, 
which should allow you to successfully navigate this section on deep learning. 
You've got this!

# Key Terms

# [Neuron]
Sometimes called a perceptron, a neuron is a graphical representation of the 
smallest part of a neural network. For the Machine Learning Crash Course we 
may reference neurons as nodes or units.

# [Gradient] π
A vector of partial derivatives. In terms of neural networks, we often use the 
analytical gradient in software and use the numerical gradient as a gradient 
checking mechanism to ensure the analytical gradient is accurate.

# [Parameter]
Any trained value in a model.

# [Feature_Transformation]
A mathematical function applied to features.

# [Hidden_layer]
A layer that's not the input or output layer in a neural network.

# [Backpropagation]
The use of the derivative chain rule along with dynamic programming to determine 
the gradients of the loss function in neural networks.

# [Forward_Pass]
Calculating an output of a neural network for a particular input.    

# [Local_Optima] π
A maxima or minima which is not the global optima.
    
# [Momentum]
A concept applied to gradient descent in which the gradients applied to the weight 
updates depends on previous gradients.
    
# [Adagrad]
An optimizer used to update the weights of a neural network in which different 
learning rates are applied to different weights.

# [Adam]
A common gradient descent optimizer that takes advantage of momentum and adaptive 
learning rates.

# [Hyperparameter]
Any parameter associated with a model which is not learned.
    
# [Optimizers]
Techniques which attempt to optimize gradient descent.
    
# [Vanishing_Gradient]
The repeated multiplication of small gradients resulting in an underflow, or 
0-value products.
    
# [Exploding_Gradient]
The repeated multiplication of large gradients resulting in an overflow, or 
infinity-value products.
    
# [Initialization_Techniques]
Ways to cleverly initialize the weights of neural networks in an attempt avoid 
vanishing and exploding gradients. Kaiming initialization, used with asymmetric 
activation functions and Xavier/Glorot initialization, used with symmetric 
activation functions are both examples. These techniques usually depend on the 
fan in and fan out per layer.
    
# [Activation_Function]
The function used on the output of a neuron. These activations can be linear or 
nonlinear. If they're nonlinear, they can be symmetric or asymmetric.

# [Rectified_Linear_Unit]
An asymmetric activation function which outputs the value of the positive inputs 
and zero otherwise. There are variations such as the Leaky ReLU. They can be 
susceptible to the dead neuron problem but generally perform well in practice.
    
# [Hyperbolic_Tangent]
A symmetric activation function which ranges from -1 to 1.
    
# [L2_Loss]
The sum of the squared errors of all the training examples. Not to be confused 
with L2 regularization.
    
# [Mean_Absolute_Error]
The average of the absolute differences across the training examples.
    
# [Dropout]
A regularization technique used per layer to reduce overfitting. Dropout involves 
randomly omitting neurons from the neural network structure at each training 
iteration. Effectively, dropout produces an ensemble of neural networks. Dropout 
is incomplete without adjusting for the dropout in preparation for prediction
    
# [Binary_Classification]
A supervised learning task in which there are two possible outputs.
    
# [Pruning_Neurons]
Removing neurons from a neural network in an effort to reduce the number of model 
parameters if by removing the neurons, equivalent performance can be obtained.
