# YouTube Sentiment

  As a data analyst for a marketing agency, your services have been requested to
  advise on the best type of content to create that has the highest potential customer
  sentiment for prospective advertisers. Using YouTube channel data, determine which
  content has the highest sentiment.

  Consider the following dataframe:

+------------+--------------------+---------------+--------+---------+
|    video_id|               title|    category_id|   likes| dislikes|
+------------+--------------------+---------------+--------+---------+
| VYOjWnS4cMY| Childish Gambino...|          Music| 5023450|   343541|
| r-3iathMo7o| The ULTIMATE $30...|     Sci & Tech|  129906|    10064|
| EAGhzuitLXU| Ed Sheeran - Sup...|          Music|  198930|     3789|
| pTysrwci0pU|     I Got A Perf...| People & Blogs|  312397|     3080|
| J6R0X6NTnSw|      Meghan Trai...|          Music|  135566|     4702|
| BQ_0QLL2gqI|  Hailee Steinfel...|          Music|  196595|     2330|
# ...
# More of the same kind of data.

  It represents information about each `video_id`.

  Use this dataframe, accessible as `video_stats_df` in the code, to create and 
  return a dataframe of the following form sorted by descending `mean_sentiment`:

+---------------+---------------+
|    category_id| mean_sentiment|
+---------------+---------------+
| Pets & Animals|             xx|
|          Shows|             xx|
|          Music|             xx|

  Sentiment here is defined as the number of likes over the total number of likes 
  and dislikes. We need to determine each category's average sentiment.

# Hints

# [Hint_1]

  First, we need to create a new column that contains the sentiment for each video.

# [Hint_2]

  Then, we need to group the videos by category.

# [Hint_3]

  Next, we need to find the average sentiment for each category.

# [Hint_4]

  Lastly, we need to create and return a dataframe that contains only the mean 
  sentiments per category and sort by those mean sentiments in descending order.
