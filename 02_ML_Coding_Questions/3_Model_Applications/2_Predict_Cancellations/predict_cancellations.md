# Predict Cancellations

  Use the `LogisticRegression` library within PySpark to predict
  subscription cancellations based on user features.

  Return the prediction dataframe produced by the `LogisticRegression` model. 
  This dataframe will contain the following columns: `rawPrediction`, which has 
  the log-odds for each example, `probability`, which has the probabilities for 
  each example, and `prediction`, which contains either a `0` or `1`, depending 
  on the probability and threshold hyperparameter.

  The prediction dataframe should be trained and predicted on the following
  dataframe:

+--------+-----------------------+----------------------+---------------------+---------------------+
| user_id|month_interaction_count|week_interaction_count|day_interaction_count|cancelled_within_week|
+--------+-----------------------+----------------------+---------------------+---------------------+
|66860ae6|                     41|                     9|                    0|                    1|
|249803f8|                     25|                     9|                    2|                    0|
|32ed74cc|                     21|                     2|                    1|                    1|
|7ed76e6a|                     22|                     5|                    2|                    0|
|46c81f43|                     32|                     8|                    2|                    0|
|cf0f185e|                     26|                     4|                    0|                    1|
|568275b3|                     29|                     5|                    1|                    1|
|86a060ec|                     33|                     7|                    1|                    1|
|c0c07290|                     35|                    10|                    0|                    0|
|709dc1da|                     36|                    11|                    1|                    0|
+--------+-----------------------+----------------------+---------------------+---------------------+
  
  The dataframe above, accessible as `user_interaction_df` in the
  code, contains features for each `user_id`, including
  `month_interaction_count`, `week_interaction_count`, and `day_interaction_count`.

  For each `user_id`, the binary label `cancelled_within_week` is `1` if the user 
  cancelled their subscription within a week of the last recorded `day_interaction_count` 
  and `0` otherwise.

  The model hyperparameters include 10 iterations, a decision threshold of 0.6,
  L1 regularization, and a regularization parameter of 0.1.
  
  Feel free to browse the PySpark `LogisticRegression` [documentation](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.classification.LogisticRegression.html).
    
# Sample Output Dataframe

+--------+--------------+------------+----------+
|user_id |rawPrediction |probability |prediction|
+--------+--------------+------------+----------+
|010b4076|         [x,x]|       [x,x]|       0.0|
|31c73683|         [x,x]|       [x,x]|       0.0|
|8173164f|         [x,x]|       [x,x]|       0.0|
|f77ad2d3|         [x,x]|       [x,x]|       0.0|
|25050522|         [x,x]|       [x,x]|       0.0|
|bfb27c75|         [x,x]|       [x,x]|       0.0|
|09663ea6|         [x,x]|       [x,x]|       1.0|
|ca7aacf2|         [x,x]|       [x,x]|       0.0|
|63f84e80|         [x,x]|       [x,x]|       0.0|
|cbb81ed7|         [x,x]|       [x,x]|       0.0|
+--------+--------------+------------+----------+

# Hints

# [Hint_1]

  First, we need to create a `"features"` column that groups the user
  features together. We can do this by using a `VectorAssembler`.

# [Hint_2]

  Then, we need to create a `"label"` column that contains all the
  labels.

# [Hint_3]

  Next, we'll create the model with the correct hyperparameters.
  `LogisticRegression` uses `elasticNetParam` to indicate
  L1, L2, or a combination of regularization strategies. Use an
  `elasticNetParam` of 1 to specify L1 regularization. We need to
  assign the decision threshold to 0.6 with the `threshold` argument.
  We then need to specify `maxIter` as 10 to limit the number of
  iterations of optimization for the model. Lastly, our regularization parameter
  `regParam` will be assigned to 0.1.

# [Hint_4]

  We then call `fit` on the `LogisticRegression` model.

# [Hint_5]

  Finally, we call `transform` on the same dataframe we trained with
  to get the predictions. This will evaluate the model's performance on the
  training examples. Make sure to ultimately select the appropriate rows
  specified in the question prompt.
