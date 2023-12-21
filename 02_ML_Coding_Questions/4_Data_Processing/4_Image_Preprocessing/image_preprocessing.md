# Image Preprocessing

  Image classification problems often require you to perform preprocessing of the
  training images to ensure that the image classification model is generalizable
  into the test and validation data sets.

  Implement and return an image preprocessing pipeline using [Tensorflow](https://www.tensorflow.org/api_docs/python/tf/keras/layers) 
  sequential layers.

  The image preprocessing pipeline should contain:

  • A resizing layer of 180x180x3

  • A rescaling layer to result in pixel values between 0 and 1

  • A random flip layer to result in horizontal and vertical augmentation

  • A random rotation layer with a factor of 0.1

  • A random contrast layer with a factor of 0.1

  • A random crop layer with a height and width factor of 0.9

  • A random zoom layer with a height and width factor of 0.1

  • A random translation layer with a height and width factor of 0.1

  • A random brightness layer with a factor of 0.1

  You will then build the pipeline with an input layer of 270x270x3 and then return
  the complied image processing pipeline.

# Hints

# [Hint_1]

  First, we need to create an empty sequential model.

# [Hint_2]

  Then, we need to insert each layer into the sequential model.

# [Hint_3]

  Next, we need to build the model and specify the input layer size.

# [Hint_4]

  Lastly, we need to return the built sequential model.
