# ML Quiz

Our practice exam to validate your machine learning knowledge.

You've gone through both crash courses. You've crushed every practice question we've thrown at you. But there's one final obstacle standing in your way: our infamous ML quiz.

It's time to put your knowledge to the ultimate test and prove that you're a true MLExpert.

The best way to assess your machine learning knowledge.

This quiz is meant to test your machine learning knowledge; it's not meant to reflect a real machine learning interview.

The quiz is difficult. We recommend going through the entire ML Crash Course and all of the Large-Scale ML sections on MLExpert first.

# Question 1 / 75
What probability distribution do multi-armed bandits rely on to determine treatment allocation?

Pareto distribution
Log-exponential distribution
Multinomial distribution
Beta distribution

# Question 2 / 75
What are some common stop words? (check all that apply):

And
Andes
It
For

# Question 3 / 75
What are some challenges with collaborative-based filtering? (check all that apply):

Silent Rooms
Cold-start problems
Echo chambers
Shilling attacks

# Question 4 / 75
What are some good ways to host features to be used for (near) real-time predictions? (check all that apply):

HDFS
Distributed cache
Low-latency database
Kafka

# Question 5 / 75
What are some ways to parallelize the training of a decision tree? (check all that apply):

Evaluate each feature in parallel
Evaluate each feature's split points in parallel
Evaluate boosted trees in parallel
Evaluate row-level nodes in parallel

# Question 6 / 75
What's the probability of drawing two consecutive spades from a deck of cards?

25%
5.8%
12.5%
3.14%

# Question 7 / 75
What are some common activation functions? (check all that apply):

Sigmoid
Hyperbolic Tangent
Rectified Linear Unit
Hyperbolic Cosine

# Question 8 / 75
If a model outputs a 68% probability of an example belonging to class 1, what decision threshold would classify that example as class 1?

80%
65%
70%
75%

# Question 9 / 75
Dropout is a technique used in neural networks to:

Reduce the number of hyperparameters
Increase the number of hyperparameters
Increase overfitting
Reduce overfitting

# Question 10 / 75
Why is having a validation set so important? (check all that apply):

To train our model outside of the training set.
To use for hyperparameter tuning outside of the test set.
To gauge the performance of the model outside of the training set.
To test our model before we perform hyperparameter tuning.

# Question 11 / 75
What's the naive independence assumption used in the Bernoulli Naive Bayes model?

There is no naive independence assumption in the Bernoulli model, only the multinomial Naive Bayes model has one.
Every word has the same prior.
Two equal words have the same prior.
The presence or absence of a word does not depend on the presence or absence of another word.

# Question 12 / 75
GANs aim to optimize which loss function?

Min-max featurizer
Adversarial softmax
Adversarial min-max
Min-max scaling

# Question 13 / 75
Exploring features, labels, and models allows us to (check all that apply):

Look into using pre-trained models
Examine feature importances
Check the completeness of data
Deploy models to production

# Question 14 / 75
What are some situations which would be suited for batch inferences? (check all that apply):

Situations where the models are not very accurate.
Situations which require substantial time to get feedback for a prediction.
Situations which don't immediately require an inference.
Situations which are extremely latency sensitive but which don't have a large number of total predictions to be calculated.

# Question 15 / 75
Which of the following are used as distance metrics? (check all that apply):

Gower distance
Simple matching distance
Euclidean distance
Manhattan distance

# Question 16 / 75
What matrix operation can be used to perform a forward pass on a fully-connected layer?

Matrix multiplication
Matrix exponentiation
Matrix transpose
Matrix inverse

# Question 17 / 75
Optimizers such as Adam are used to:

Optimize the model hyperparameters with respect to a loss function
Optimize the model hyperparameters with respect to the regularizer
Optimize the model parameters with respect to a loss function
Optimize the model parameters with respect to the regularizer

# Question 18 / 75
RNNs allow for:

No hidden states
No needed hyperparameter tuning
Variable sized inputs and outputs
Entirely stable gradients

# Question 19 / 75
What matrix operation can be used to perform a convolution?

Matrix exponentiation
Matrix inverse
Matrix multiplication
Matrix transpose

# Question 20 / 75
What are some common examples of data ingestion? (check all that apply):

Change data capture
Clickstream
Live video
Batch ingestion

# Question 21 / 75
The concept of a DAG, or directed acyclic graph, is used in which technologies? (check all that apply):

Spark
HDFS
Kafka
Airflow

# Question 22 / 75
What are some requirements for A/B testing? (check all that apply):

At most one treatment
Exactly one control
At least one treatment
At least two controls

# Question 23 / 75
What are the things you should consider when building a data ingestion system? (check all that apply):

Rate at which individual data comes in
High-availability and fault tolerance
Size of individual data
Support of data types

# Question 24 / 75
What factors influence a confusion matrix? (check all that apply):

True Negatives
False Negatives
False Positives
True Positives

# Question 25 / 75
Boosting a decision tree model will most likely:

Reduce the error caused by variance
Reduce the error caused by bias
Increase the error caused by bias
Increase the error caused by variance

# Question 26 / 75
Which of the following need to be synchronized when deploying a model to production? (check all that apply):

Feature serving deployment
Model deployment
Training deployment
Software environment deployment

# Question 27 / 75
What is one way to parallelize the training of a logistic regression model?

Distribute the regularizers across multiple machines and train each regularizer on parts of a minibatch.
Distribute the model across multiple machines and train each machine on parts of a minibatch.
Distribute the minibatch across multiple machines and train each minibatch on parts of the hyperparameters.
Distribute the hyperparameters across multiple machines and train each hyperparameter on parts of a minibatch.

# Question 28 / 75
What are some critical components of HDFS? (check all that apply):

Name Node
Data Node
HDFS client
Journal Node

# Question 29 / 75
What machine learning model is most closely related to a neuron in a neural network?

K-nearest neighbors
Logistic regression
SVM
Naive Bayes

# Question 30 / 75
What are some ways to represent users in an A/B test? (check all that apply):

Device ID
Session cookie
IP address
User ID

# Question 31 / 75
What are some components of YARN? (check all that apply):

Container
Node Manager
Application Master
Resource Manager

# Question 32 / 75
Why is normalized discounted cumulative gain a useful tool in ranking models?

NDCG is typically used to score a particular ranking such that an incrementally lower score is given to relevant documents as they appear at a lower rank.
NDCG is typically used to score a particular ranking such that an incrementally lower score is given to relevant documents as they appear at a higher rank.
NDCG is typically used to score a particular ranking such that an incrementally higher score is given to relevant documents as they appear at a higher rank.
NDCG is typically used to score a particular ranking such that an incrementally higher score is given to relevant documents as they appear at a lower rank.

# Question 33 / 75
What are some ways to parallelize user-item matrix factorization? (check all that apply):

Distribute the user-item matrix across multiple machines to reduce the total number of training examples required.
Distribute the user-item matrix across multiple machines to reduce the total number of calculations required.
Distribute the user-item matrix across multiple machines to parallelize the calculations.
Distribute the user-item matrix across multiple machines to reduce the memory requirements per machine.

# Question 34 / 75
What are some important components of a hypothesis? (check all that apply):

Independent variable
Dependent variable
Making sure the hypothesis turns out to be true
Participants

# Question 35 / 75
What are some common data processing techniques? (check all that apply):

Joins
Aggregations
Compilations
Transformations

# Question 36 / 75
What is a common use for the Gini Impurity metric?

To evaluate the effectiveness of a split point in a classification tree
To evaluate the effectiveness of boosting in a regression tree
To evaluate the effectiveness of a split point in a regression tree
To evaluate the effectiveness of boosting in a classification tree

# Question 37 / 75
What are some concepts associated with frequentist A/B testing? (check all that apply):

Significance
Power
Sample size
Minimum detectable change

# Question 38 / 75
What does the total area under the model's receiver operating characteristic curve represent?

The probability that a randomly chosen positive example will have a higher prediction probability of being positive than a randomly chosen negative example.
The probability that a randomly chosen positive example will be classified correctly.
The probability that a randomly chosen example will be classified incorrectly.
The probability that a randomly chosen positive example will have a lower prediction probability of being positive than a randomly chosen negative example.

# Question 39 / 75
What's the difference between a hard-margin and soft-margin SVM?

Soft-margin SVMs introduce a slack variable which allows some points to lie on the wrong side of the margin.
Hard-margin SVMs introduce a regularization variable that encourages all points to lie on the wrong side of the margin.
Soft-margin SVMs introduce a regularization variable that encourages all points to lie on the wrong side of the margin.
Hard-margin SVMs introduce a slack variable which allows some points to lie on the wrong side of the margin.

# Question 40 / 75
Bagging a decision tree model will most likely:

Increase the error caused by variance
Reduce the error caused by bias
Reduce the error caused by variance
Increase the error caused by bias

# Question 41 / 75
CNNs are variations of fully-connected neural networks which:

Increase the number of required parameters through dropout, scaling, and batch gradient descent
Reduce the number of required parameters through weight sharing, strides, and pooling.
Reduce the number of required parameters through dropout, scaling, and batch gradient descent
Increase the number of required parameters through weight sharing, strides, and pooling.

# Question 42 / 75
What are some common techniques of feature scaling? (check all that apply):

Extreme scaling
Min-max scaling
Standardization
Median scaling

# Question 43 / 75
Which of the following are ways to perform hyperparameter tuning? (check all that apply):

Feature optimization
Random search
Grid-search
Bayesian optimization

# Question 44 / 75
What does a p-value represent?

The probability that the observed result (or a more extreme result) could have been observed in the case that the null hypothesis is correct.
The probability that the observed result (or a more extreme result) could have been observed in the case that the alternative hypothesis is correct.
The probability that the observed result (or a more extreme result) could have been observed in the case that neither the alternative or null hypotheses are correct.
The probability that the observed result (or a more extreme result) could have been observed in the case that both the alternative and null hypotheses are correct.

# Question 45 / 75
TF-IDF is a technique which represents text as:

The frequency of each word as it appears across all documents.
The frequency of each word as it appears in a given document.
The relative importance of each document across all documents.
The relative importance of each word in a given document.

# Question 46 / 75
What are some components of Apache Airflow? (check all that apply):

DAG store
Scheduler
Worker
Webserver

# Question 47 / 75
Features can be of the following types (check all that apply):

Abnormal
Categorical
Ordinal
Numerical

# Question 48 / 75
Why is a softmax useful?

It's a common activation function used to signal upstream neurons on whether or not to activate.
It allows us to transform a series of scores-per-class to a probability distribution across the classes.
It's a common activation function used to signal downstream neurons on whether or not to activate.
It allows us to transform a probability distribution across the classes to a series of scores-per-class.

# Question 49 / 75
Limiting the depth of a decision tree will most likely:

Increase the number of required training examples
Increase overfitting
Reduce the number of required training examples
Reduce overfitting

# Question 50 / 75
Why is regularization useful?

It enforces hyperparameters of a model to take on reasonable values which can prevent overfitting.
It enforces hyperparameters of a model to take on reasonable values which can prevent underfitting.
It enforces parameters of a model to take on reasonable values which can prevent overfitting.
It enforces parameters of a model to take on reasonable values which can prevent underfitting.

# Question 51 / 75
What are some metrics we could use to measure the business impacts of an A/B test? (check all that apply):

Click through rate/probability
Purchase rate
Sign-up rate
Ingestion rate

# Question 52 / 75
What are some common tools used to facilitate producers and consumers in data ingestion? (check all that apply):

Kinesis
HDFS
PostgreSQL
Kafka

# Question 53 / 75
Auto-ML aims to provide (check all that apply):

Automated feature selection
Automated model selection
Automated data collection
Automated hyperparameter tuning

# Question 54 / 75
What is the difference between content-based and collaborative-based filtering?

Collaborative-based filtering doesn't rely on any data to form predictions. Content-based filtering requires all features from all users to form a single user's predictions.
Content-based filtering doesn't rely on other users' data to form predictions. Collaborative-based filtering doesn't require features of a particular item or user.
Collaborative-based filtering doesn't rely on other users' data to form predictions. Content-based filtering doesn't require features of a particular item or user.
Content-based filtering doesn't form predictions. Collaborative-based filtering only forms a single prediction for a single user.

# Question 55 / 75
Which one of the following is considered a 2-gram or bigram?

Professional baseball game
Baseball
Baseball game
Game

# Question 56 / 75
An interaction term is useful in a regression model when:

A dependent variable has a different effect on the outcome depending on the values of another dependent variable.
An independent variable has a different effect on the outcome depending on the values of another independent variable.
A dependent variable has the same effect on the outcome depending on the values of another dependent variable.
An independent variable has the same effect on the outcome depending on the values of another independent variable.

# Question 57 / 75
What's the difference between a local minimum and a global minimum?

A local minimum is guaranteed to be the minimum value across the entire function while a local global is not.
A global minimum is guaranteed to be the maximum value across the entire function while a local minimum is not.
A local minimum is guaranteed to be the maximum value across the entire function while a local global is not.
A global minimum is guaranteed to be the minimum value across the entire function while a local minimum is not.

# Question 58 / 75
What probability distribution does Bayesian A/B testing rely on to form the posterior?

Pareto distribution
Multinomial distribution
Log-exponential distribution
Beta distribution

# Question 59 / 75
What is PCA?

A method for finding orthogonal lines which best fit each dimension of the data.
A method for finding parallel lines which best fit each dimension of the data.
A method for finding parallel lines which best fit each data point in the data set.
A method for finding orthogonal lines which best fit each data point in the data set

# Question 60 / 75
What is one benefit of using a multi-armed bandit to test your hypothesis?

Support only a single hypothesis to be tested at a time.
Minimize the p-value during the experiment.
Enable a tunable way to explore a hypothesis while also exploiting what works best.
Maximize the regret during the experiment.

# Question 61 / 75
What is generally true about GPUs?

They're more general purpose than CPUs.
They're faster than CPUs for single computations.
They have fewer cores than CPUs.
They have higher throughput than CPUs.

# Question 62 / 75
The Gaussian Naive Bayes model is trained based on the following (check all that apply):

The median of each of the features.
The mean of each of the features.
The standard deviation of each of the features.
The outliers of each of the features.

# Question 63 / 75
What is the best use for a model's receiver operating characteristic curve?

To tune the size of training set
To tune the trained model parameters
To tune the decision threshold of the model
To tune the size of the validation set

# Question 64 / 75
The logistic function outputs values in the range of:

[-1, 1]
[0,1]
[-1, 0]
[1, 2]

# Question 65 / 75
What are some common parallelism approaches to training deep models? (check all that apply):

Feature parallelism
Label parallelism
Data parallelism
Model parallelism

# Question 66 / 75
What are the relevant terms in Bayes' theorem? (check all that apply):

The posterior.
The prior.
The evidence.
The likelihood.

# Question 67 / 75
How does the curse of dimensionality affect distance metrics?

As the number of dimensions grows, common distance metrics produce smaller distances between samples.
As the number of examples grows, the number of distance metrics used must increase.
As the number of examples grows, common distance metrics produce larger distances between samples.
As the number of dimensions grows, the number of distance metrics used must increase.

# Question 68 / 75
Why is a confidence interval useful in the case of linear regression coefficients?

It provides a range around the value of the input which represents the uncertainty of the input.
It provides a range around the value of the coefficient which represents the uncertainty of the coefficient.
It provides a range around the value of the label which represents the uncertainty of the label.
It provides a range around the value of the features which represents the uncertainty of the features.

# Question 69 / 75
What are some components of Apache Spark? (check all that apply):

Cluster Manager
Executor
Delegator
Driver

# Question 70 / 75
A high specificity means that a model will:

Aim to produce a low variance.
Aim to produce a high variance.
Aim to produce fewer false positives than false negatives.
Aim to produce fewer false negatives than false positives.

# Question 71 / 75
Which one of the following is a decentralized deep model training strategy?

Ring all-reduce
Feature Store
Hyperparameter server
Parameter server

# Question 72 / 75
What are some benefits of using a heuristic over machine learning? (check all that apply):

Heuristics can be used to quickly improve the performance of a machine learning model.
Heuristics are often easier to debug.
You can use heuristics before implementing a machine learning model to test your hypothesis.
You can be sure a heuristic is working without measuring its performance.

# Question 73 / 75
Avro is ______-oriented while Parquet is _____-oriented.

feature, data
row, column
column, row
data, feature

# Question 74 / 75
What are some things to consider after running an experiment? (check all that apply):

Extrapolation appropriateness
Experiment collisions
Bias correction
Cost of experimentation

# Question 75 / 75
What are some things to consider before running an experiment? (check all that apply):

Cost of experimentation
Determining if the experiment results are valid
Potential benefit to customers/company
Risk to customers/company
