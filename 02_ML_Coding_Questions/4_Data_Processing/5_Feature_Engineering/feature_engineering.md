# Feature Engineering

  You're a data scientist for a real estate division of an investment bank. Given
  the data following data, perform feature engineering that results in a dataframe
  that can be used in a model to predict the tax liabilities for a particular home.

  The format of the `df_houses`  dataframe is:

  +---------+---------------+---------------+------------+---------------+------+-------------------+
  | (index) | avg_room_sqft | avg_bath_sqft | land_value | tax_liability | year | location          |
  +---------+---------------+---------------+------------+---------------+------+-------------------+
  | 0       | 39.1          | 18.7          | 181000.0   | 3750.0        | 2007 | "Los Angeles, CA" |
  | 1       | 39.5          | 17.4          | 186000.0   | 3800.0        | 2007 | "Chicago, IL"     |
  | 2       | 40.3          | 18.0          | 195000.0   | 3250.0        | 2007 | "Chicago, IL"     |
  | 3       |               |               |            |               | 2007 | "Houston, TX"     |
  | 4       | 36.7          | 19.3          | 193000.0   | 3450.0        | 2007 | "Chicago, IL"     |
  | 5       | 39.3          | 20.6          | 190000.0   | 3650.0        | 2007 | "Houston, TX"     |
  | 6       | 38.9          | 17.8          | 181000.0   | 3625.0        | 2007 | "Phoenix, AZ"     |
# ...
# More of the same kind of data.

  Implement `get_features` to impute the following missing column values
  with the location's averages:

  • tax_liability

  • land_value

  • avg_bath_sqft

  • avg_room_sqft

  As well, `get_features` should perform one-hot encoding for the following
  columns:

  • year

  • location

  Finally, perform min-max scaling for each column in the dataframe.

  The columns of the result returned from `get_features` should be in the order of:

  • avg_room_sqft

  • avg_bath_sqft

  • land_value

  • tax_liability

  • 2007

  • 2008

  • 2009

  • Chicago, IL

  • Dallas, TX

  • Houston, TX

  • Los Angeles, CA

  • New York City, NY

  • Philadelphia, PA 

  • Phoenix, AZ

  • San Antonio, TX

  • San Diego, CA

  • San Jose, CA

# Hints

# [Hint_1]

  First, we need to impute the missing values of for the columns listed in the prompt.
  This requires use to group the rows by location and then find the mean. Of each column.
  Finally, we need to assign these means to the missing values.

# [Hint_2]

  Then, we need to one-hot encode the other columns listed in the prompt. This
  means creating dummy values for those columns and then dropping the original
  columns.

# [Hint_3]

  Finally, we need to min-max scale all the values in the dataframe. This means
  subtracting the min value for each column from each columns value and then dividing
  these values by the range of each column's respective values.
