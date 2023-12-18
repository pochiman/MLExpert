# 14 - Convolutional Neural Networks

Convolutional, but not necessarily convoluted.
Don't you love our witty epigrams?

# Key Terms

# [Fully_Connected_Neural_Network]
A neural network that has every neuron connected to every other neuron in the 
subsequent layer; also called a dense layer.

# [Image_Kernel]
A single array consisting of some defined numbers, which is applied to an image 
for some desired effect. Usually used in the context of image filtering.

# [Image_Padding]
Adding a border of zero-valued pixels to an input image. The goal of padding is 
typically to ensure that the dimensions of an image remain the same after applying 
an image kernel. Libraries typically allow two options: Valid Padding, which means 
not to pad the image, and Same Padding, which means to zero-pad the image.

# [Convolutional_Layer]
Similar to a fully connected neural layer; however, each neuron is only connected 
to a subset of neurons in the subsequent layer with respect to a receptive field.

# [Receptive_Field]
The number of neurons in a preceding layer which are connected to an adjacent layer 
of neurons. The largest receptive field is a fully-connected neural network.

# [Stride]
The incremental rate at which a kernel is applied to an image or feature map.

# [Feature_Map]
The result of applying a kernel to an image or to another feature map.

# [Channels]
The number of stacked images, typically representing Red Green Blue pixels, or 
the number of feature maps produced by a convolutional layer.

# [Pooling]
Most often max pooling and sometimes average pooling, in which a kernel is applied 
to an image and the max or average of the pixel values in the kernel overlay is 
the resulting pixel value in the output image.

# [Shift_Invariance]
One of the goals of a convolutional neural network: objects within an image can 
be in different areas of the image yet still be recognized.

# [Flatten_Layer]
Takes in a series of stacked feature maps and flattens out all of the values into 
a single feature vector.

# [Mechanical_Turk]
A crowdsourcing service which performs on-demand tasks that computers are currently 
unable to do.

# [Batch_Normalization]
The process of normalizing values by means of re-centering (subtracting the mean) 
or re-scaling (dividing by the standard deviation) before they go to subsequent 
layers in a neural network. The goal is to accelerate the learning of deep neural 
networks by decreasing the number of epochs required for the loss function to 
converge.

# [Keras] ϟ
Software that acts as an interface for Tensorflow and aims to simplify the experience 
of working with neural networks.

# [Graphics_Processing_Unit]
A specialized device that has many cores, allowing it to perform many operations 
at a time.

GPUs are often used within deep learning to accelerate training of neural networks 
by taking advantage of their ability to perform many parallel computations.

# [Pre-trained_Models]
Models which have already been trained. These trained models can be used as layers 
(like embedding layers) of not-yet-trained neural networks to increase performance 
of these neural network.
