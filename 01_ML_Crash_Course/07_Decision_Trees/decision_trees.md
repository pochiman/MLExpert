# 7 - Decision Trees
Yes or no? That is the question.
Literally.

# Key Terms

# [Decision_Tree]
A tree-based model which traverses examples down to leaf nodes by the properties 
of the examples features.

# [Sample_Size]
The number of observations taken from a complete population.

# [Classification_and_Regression_Tree]
Also CART, is an algorithm for constructing an approximate optimal decision tree 
for given examples.

# [Missing_Data]
When some features within an example are missing.

# [Split_Point]
A pair of feature and feature value which is assigned to a node in a decision tree. 
This split point will determine which examples will go left and which examples go 
right based on the feature and feature value.    

# [Gini_Impurity]
Used as a way to determine the best split point for a given node in a classification 
tree. It's based on the probability of incorrectly classifying an item based on all 
of the items in the node.

# [Surrogate_Split]
A suboptimal split point reserved for examples which are missing the optimal split 
point feature.

# [Mean_Squared_Error]
The average squared difference between the prediction and true label across all 
examples.

# [Boosting]
An ensemble technique which trains many weak learners sequentially, with each 
subsequent weak learner being trained on the previous weak learner's error. 
This generally reduces the bias error.

# [Bagging]
Also bootstrap aggregation, a sampling technique which selects subsets of examples 
and/or features to train an ensemble of models. This generally reduces the variance 
error.

# [Weak_Learner]
Shallow decision trees in our case. However, it generally can be any underfitting 
model.

# [Ensemble]
Using more than one model to produce a single prediction.

# [Random_Forest]
An ensemble technique which trains many independent weak learners. This generally 
reduces the variance error.

# [XGBoost] ϟ
An open-source library which provides a gradient boosted framework. Short for Extreme 
Gradient Boosting.

# [LightGBM] ϟ
An open-source library created by Microsoft which provides a distributed gradient 
boosted framework. Short for Light Gradient Boosted Models.
