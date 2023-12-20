# B2B SVD

  Visa wants to incentivize small and medium businesses (SMBs) to apply for business
  credit cards. A product manager within Visa decided to offer business rewards
  for SMBs when they conduct transactions with partnered enterprises. Visa has a
  transaction database which stores transaction information such as average transaction
  amount and frequency of transactions between SMBs and enterprises. Using the
  provided dataframes, provide the product manager the top 10 enterprises Visa should
  partner with to entice SMBs to apply for Visa business credit cards.

  You’re given two Pandas dataframes. The first dataframe contains the number of monthly
  transactions each SMB conducts with each respective enterprise. The rows represent each
  SMB and the columns represent each enterprise. This is a sparse dataframe.

   +--------+-----+----+----+----+----+
   | (index)|  TXT| HFC| CMI| CCL| HRB| ...
   +--------+-----+----+----+----+----+
   |      40|    3|   0|   5|   0|   0| ...
   |      57|    0|   8|   6|   0|   0| ...
   |      69|    0|   0|   0|   9|   0| ...
   |      43|    0|   1|   0|   0|   1| ...
   |      64|    4|   0|   0|   1|   4| ...
  # ...
  # More of the same kind of data.

  The second dataframe contains the average transaction amount each SMB conducts
  with each respective enterprise. The rows represent each SMB and the columns
  represent each enterprise. This is a sparse dataframe and only has values where
  the above dataframe has non-zero values.

   +--------+--------+--------+--------+--------+--------+
   | (index)|     TXT|     HFC|     CMI|     CCL|     HRB| ...
   +--------+--------+--------+--------+--------+--------+
   |      40|  342.84|       0|   56.82|       0|       0| ...
   |      57|       0|   99.83|   14.82|       0|       0| ...
   |      69|       0|       0|       0|  567.22|       0| ...
   |      43|       0|  243.66|       0|       0|  144.89| ...
   |      64|  781.72|       0|       0|  456.12|  982.23| ...
  # ...
  # More of the same kind of data.

  Use these two dataframes to derive a new dataframe that contains the average total
  monthly transaction amount. This resultant dataframe will be used on scikit-learn’s 
  [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html). The output of the TruncatedSVD will be an embedding for each enterprise. The top 10
  enterprises for Visa to partner with will have the maximum embedding values. 

  The list of the top 10 enterprises that you return will be evaluated against the ground truth
  set using the Jaccard similarity. The Jaccard similarity between your answer and
  the ground truth must be greater than 66%.

# Sample Output

['TXT', 'HFC', 'CMI', ... 'HRB']

# Hints

# [Hint_1]

  First, we need to derive the average monthly total enterprise transactions for
  each SMB. We can do this by element-wise multiplying `avg_trxn_amount` by 
  `num_monthly_trxn`.

# [Hint_2]

  Then, we need to use `TruncatedSVD` on the transposed resultant dataframe
  from the previous hint. This will produce the enterprise embeddings. Only 10 components
  should be used when defining the embedding size because we want the top 10 enterprises
  to partner with.

# [Hint_3]

  After fitting the `TruncatedSVD` to the enterprises, we need to determine
  the indices with the highest embedding values. We can accomplish this by using
  `argmax(axis=0)`. These indices will allow us to get the top 10 enterprises.

# [Hint_4]

  Lastly, we need to map the top 10 enterprise embedding values to the actual ticker
  of the enterprise. These ticker values are what will be returned from the function.
  We can accomplish this by using `iloc` on the transposed dataframes of
  either `avg_trxn_amount` or `num_monthly_trxn`.
