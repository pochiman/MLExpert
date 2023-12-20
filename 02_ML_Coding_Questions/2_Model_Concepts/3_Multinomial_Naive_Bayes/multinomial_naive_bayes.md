# Multinomial Naive Bayes

  Create a multinomial Naive Bayes classifier to add tags to articles, where
  tags represent categories that articles should belong to.

  You'll have access to training articles inside of a dictionary `MultinomialNB.articles_per_tag` 
  mapping tags to the articles belonging to said tags.

  Below is an example portion of the `MultinomialNB.articles_per_tag`:
  
{
  "politics": [
    ["article", "writes", "Joel", "Furr", "writes", # ... more words],
    ["Distribution", "world", "following", "posted", # ... more words],
    # ...
    # More articles.
    ],
    "sports": [
    ["article", "writes", "just", "wanted", # ... more words],
    ["Phillies", "salvaged", "their", "weekend", # ... more words],
    # ...
    # More articles.
    ],
    "tech": [
    ["Thanks", "Steve", "your", "helpful", # ... more words],
    ["Please", "unsubscribe", "This", "user", # ... more words],
    # ...
    # More articles.
  ],
} 

  Note that:

  • The Laplacian smoothing hyperparameter has been chosen to be `1`, 
    which means that when calculating likelihoods, you'll be adding `2` 
    to the denominator and `1` to the numerator.

  • If an input to the model contains a word that is not in the trained Naive
    Bayes model, that word should be assigned a class probability of 50%.
  
  • You shouldn't use TF-IDF. 
  
  • You shouldn't use any libraries that implement the multinomial Naive Bayes
    classifier for you, such as scikit-learn.

  • You're encouraged to use the `collections` module as well as the
    `math` module.

  • Your output values will automatically be rounded to the fourth decimal.

  If you're unfamiliar with Naive Bayes classifers, we recommend watching the
  Naive Bayes video in the ML Crash Course on MLExpert before starting to code.

# Sample Input

article = [
  "article", "writes", "while",
  "when", "owned", "Plus",
  "wanted", "upgrade", "memory",
  "just", "ordered", "toolkit",
  "from", "Macwarehouse", "something",
  "like", "included", "antistatic",
]

# Sample Output

{
  "politics": -91.3016,
  "sports": -87.1427,
  "tech": -85.1920
}
# The log probability for each article tag.

# Hints

# [Hint_1]

  Think about what terms are needed to calculate the Naive Bayes posterior.
  Remember that you'll only need to calculate the numerator of each tag; the
  most probable tag produces the highest numerator.

# [Hint_2]

  Start training the model by calculating the prior for each tag. That's the log
  probability of getting each tag, regardless of the article content. This means
  counting the number of articles per tag and dividing by the total number of
  articles across all tags.

# [Hint_3]

  Besides the prior, the other required term for training the multinomial Naive
  Bayes model is the multinomial likelihoods per tag. This means, for each word,
  counting the occurrences of the word in the tag and dividing that count
  by the total number of words in the tag. Don't forget Laplacian smoothing.

# [Hint_4]

  Now that the likelihood per word per tag is calculated along with the prior of
  each tag, we can form a prediction given an input. For each tag, and for each
  word in the input, we have to find the total log likelihood of that particular
  input belonging to a particular tag.

# [Hint_5]

  To find the log likelihood for a given input, iterate through each word in the
  input, and look up each word's log likelihood for a given tag that you're
  calculating.

# [Hint_6]

  After you've found the log likelihood, don't forget to add the tag prior to
  find the posterior.
