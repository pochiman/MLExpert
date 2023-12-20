# Classify Trucks

  Create and return a convolutional neural network (CNN) to classify images
  produced by a traffic-camera feed based on whether or not a truck is in the
  images.

  Note that:

  • You should use TensorFlow 2 Keras APIs to create a CNN that expects images
    of dimensions `224x224` with 3 channels (Red, Green, and Blue). 
  
  • The CNN should consist of `8` ordered layers:

    1. A convolutional layer with `16` filters, each with a kernel of
        dimensions `3x3` and a Rectified Linear Unit (ReLU) activation
        function.
    
    2. A max pooling layer with dimensions `2x2`.

    3. A convolutional layer with `32` filters, each with a kernel of
        dimensions `3x3` and a ReLU activation function.
    
    4. Another max pooling layer with dimensions `2x2`.

    5. A convolutional layer with `64` filters, each with a kernel of
        dimensions `3x3` and a ReLU activation function.
    
    6. A layer to flatten the values of the previous layer.

    7. A dense layer (fully connected) with `20` neurons and a ReLU
        activation function.
      
    8. Finally, a dense layer with a single neuron and sigmoid activation. This 
        layer will output the prediction.

  • Each convolutional and pooling layer should use valid padding, each layer
    with a ReLU activation should use He normal initialization, and the layer
    with a sigmoid activation should use Glorot normal initialization.
  
  • The CNN should use Adam as the optimizer with a learning rate of `.01`. As 
    well, binary cross-entropy should be used as the loss function, since the 
    label of each frame is `1` when there's a truck in the image and `0` when 
    there isn't a truck in the image.

  The following two images are example images that will be used to train your
  model:

  • 02_ML_Coding_Questions/3_Model_Applications/1_Classify_Trucks/classify_trucks_with_truck.jpg
  • 02_ML_Coding_Questions/3_Model_Applications/1_Classify_Trucks/classify_trucks_without_truck.jpg

  The first image would be labeled as `1`, since a truck is in the
  image. Conversely, the second image would be labeled as `0`, since
  there isn't a truck in the image.

  The training will be handled for you. You're only required to return the model
  with the above specifications. Be sure to include binary accuracy as the
  metric to monitor during training.

# Hints

# [Hint_1]

  First, we need to create a Sequential model provided by TensorFlow's
  high-level API, Keras.

# [Hint_2]

  We can provide the Sequential model with a list of layers that we want to
  include in the CNN.

# [Hint_3]

  The first layer will be a convolutional layer, which is availble in Keras as
  `Conv2D`. We need to speciy the Rectified Linear Unit (ReLu)
  activation function which can be done by assigning the
  `activation` parameter the value of `'relu'`.

# [Hint_4]

  As well, we also have to specify an `input_shape` parameter, which
  will allow the `Conv2D` layer to know what to expect in terms of
  input. For this scenario, we want to specify a tuple
  `(224, 224, 3)`, which contains the image dimensions followed by
  the three channels, RGB—one for each color channel in the images.

# [Hint_5]

  We want to use He normal initialization for the first layer. To do that we
  need to set the `kernel_initializer` parameter as
  `'he_normal'`.

# [Hint_6]

  Next, we want a max pooling layer, specified by `MaxPooling2D` in
  Keras.

# [Hint_7]

  When we get to the flatten layer, we need to use `tf.keras.layers.Flatten()`.

# [Hint_8]

  When we get to the first dense layer, we need to use `Dense` in
  Keras.

# [Hint_9]

  Finally, the output layer will be a dense layer as well. It'll have a single
  neuron, a sigmoid activation, and use `'glorot_normal'` initialization.

# [Hint_10]

  Once the model is defined, we need to compile the model with an optimizer, a
  loss, and a metric that we want to monitor during training.

# [Hint_11]

  To do that, we can use the `compile` function on the model. It
  takes in an `optimizer` (in our case, Adam), a
  `BinaryCrossentropy()` as its `loss`, and
  `['binary_accuracy']` as its `metrics`.
