# Ranking

# 18 - Learning To Rank

Rank your top five ML models.
Did you use a ranking model to rank your models?

# Key Terms

# [Candidate_Generator]
A system which outputs the candidates to be ranked. This is sometimes referred to as retrieving the ‘top-k'.

# [Embedding_Space]
The n-dimensional space where embeddings exist. Typically, the embedding space can 
be used to generate the top-k candidates by using the k-nearest neighbors algorithm.
    
# [Cosine_Similarity] π
A similarity metric which is equal to the cosine of the angle between two inputs in 
some embedding space.
    
# [Linear_Activation]
A symmetric activation function which assigns the output as the value of the input.
    
# [Normalized_Discounted_Cumulative_Gain]
An information retrieval metric which assigns a value of a particular ranking based 
on each item's position and relevance.
    
# [Mean_Average_Precision]
A binary ranking metric which takes into account the relevance of ranked items with 
regards to their position.
    
# [Mean_Reciprocal_Rank]
A binary ranking metric which takes into account the first spot in a ranking which 
contains a relevant item.
    
# [Shrinkage]
A learning rate for gradient boosted trees.
    
# [Side_Features]
Features in addition to item and user embeddings. This can include properties of 
items and users.
    
# [Implicit_Relevance_Feedback]
Feedback obtained from user behavior as opposed to surveying the user.

# [Presentation_and_Trust_Bias]
Biases found within ranking which arise from the placement of items within a ranking.
