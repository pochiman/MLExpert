# TLDR

  You’re the founding engineer of TLDR, a startup that publishes summarized book
  chapters to a subscriber base. The startup’s core product offering provides
  users a daily newsletter containing a chapter summary of the user’s chosen books.
  Write a function which takes in text and returns an extractive summary.

text_to_summarize =
  "
    Those Who Are Resilient Stay In The Game Longer ...
    ... I recall a passage my father often used when I was growing up in the 1990s ...
    ... Nurture your dreams ... Angela Duckworth who writes in Grit ...
  "

# Sample Output

  "
    Those Who Are Resilient Stay In The Game Longer ...
    Angela Duckworth who writes in Grit ...
  "

  Use NLTK (https://www.nltk.org/) and scikit-learn’s [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to perform the extractive summarization.

  Your summary will be evaluated using [ROUGE](https://en.wikipedia.org/wiki/ROUGE_(metric)) 
  or Recall-Oriented Understudy for Gisting Evaluation. Specifically, ROUGE-L
  f-score will be used as the primary metric when comparing the ground truth summary
  to your summary. ROUGE-L measures the longest common subsequence (LCS) between two
  reference texts. Longer shared subsequences indicate more similarity between the
  two sequences. The precision and recall of ROUGE-L will be used to calculate the
  final ROUGE-L f-score.

  Your summary must:

  • Score a ROUGE-L f-score of greater than 60% when compared to the ground truth.

  • Be no longer than 50% of the document.

# Hints

# [Hint_1]

  First, we need to tokenize sentences out of the input text. We can use `sent_tokenize` 
  from the `nltk` library.

# [Hint_2]

  Then, we need to use `TfidfVectorizer` on the tokenized sentences.
  We should be sure to provide `stopwords` from `nltk.corpus` 
  to the vectorizer so that the vectorizer ignores stop words.

# [Hint_3]

  After fitting and transforming the input text with `TfidfVectorizer`,
  we need to then find the sentences with the maximum values of tf-idf. We can get
  this by summing through the vecotorizer result. The higher the sentence tf-idf
  sum, the more likely that sentence is to be included in the summary.

# [Hint_4]

  Then, we need to identify a threshold of sentence tf-idf sums. This threshold
  will be used to decide whether to include or exclude particular sentences from
  the summary. The threshold should take on a value which enables the function to
  meet both requirements of the summary: length and ROUGE score.

# [Hint_5]

  Finally, we need to assemble and return the summary based on the sentences which have
  a higher tf-idf sum than the threshold.
