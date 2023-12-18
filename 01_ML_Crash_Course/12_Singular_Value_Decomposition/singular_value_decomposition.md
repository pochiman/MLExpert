# 12 - Singular Value Decomposition

As you've probably noticed, we like to keep these blurbs light and cheeky. Unfortunately, despite our best attempts, we simply could not find humor in "singular value decomposition." So here's a cute ASCII bear instead:  

ʕ •ᴥ•ʔ

# Key Terms

# [Singular_Value_Decomposition]
Also SVD, a process which decomposes a matrix into rotation and scaling terms. 
It is a generalization of eigendecomposition.

# [Rank_r_Approximation]
Using up to, and including, the rth terms in the singular value decomposition to 
approximate an original matrix.

# [Dimensionality_Reduction]
The process of reducing the dimensionality of features. This is typically useful 
to speed up the training of models and in some cases, allow for a wider number of 
machine learning algorithms to be used on the examples. This can be done with SVD 
(or PCA) and as well, certain types of neural networks such as autoencoders.

# [Eigendecomposition] π
Applicable only to square matrices, the method of factoring a matrix into its 
eigenvalues and eigenvectors. An eigenvector is a vector which applies a linear 
transformation to some matrix being factored. The eigenvalues scale the eigenvector 
values.

# [Principal_Component_Analysis]
Also PCA, is eigendecomposition performed on the covariance matrix of some particular 
data. The eigenvectors then describe the principle components and the eigenvalues 
indicate the variance described by each principal component. Typically, SVD is used 
to perform PCA. PCA assumes linear correlations in the data. If that assumption is not 
true, then you can use kernel PCA.

# [Orthogonal] π
Perpendicular is n-dimensions.
