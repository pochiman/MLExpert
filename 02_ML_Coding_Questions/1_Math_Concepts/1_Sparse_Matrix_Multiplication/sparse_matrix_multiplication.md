# Sparse Matrix Multiplication

  Write a function that takes in two integer matrices and multiplies them
  together.

  Both matrices will be sparse, meaning that most of their elements will be
  zero. Take advantage of that to reduce the number of total computations that
  your function performs.

  If the matrices can't be multiplied together, your function should return [[]].

# Sample Input

matrix_a = [
  [0,  2, 0],
  [0, -3, 5],
]
matrix_b = [
  [0, 10, 0],
  [0,  0, 0],
  [0,  0, 4],
] 

# Sample Output

[
  [0, 0,  0],
  [0, 0, 20],
]

# Hints

# [Hint_1]

  Matrices A and B can only be multiplied together if the number of columns in
  matrix A is equal to the number of rows in matrix B.

# [Hint_2]

  Matrix C, resulting from multiplying matrices A and B together, has the number
  of rows that matrix A has and the number of columns that matrix B has.

# [Hint_3]

  The element at position `i, j` in matrix C, resulting from multiplying matrices 
  A and B together, is the dot product of the ith row of A and the jth column of B. 
  In other words, 
  `c[i, j] = a[i][0] * b[0][j] + a[i][1] * b[1][j] + ... + a[i][k] * b[k][j]`
  
# [Hint_4]

  Since a lot of elements in the matrices are zero, you can use sparse
  representations of the matrices to quickly detect zeroes and to then skip
  operations that involve multiplications with a zero. This can drastically
  reduce the total number of operations performed by your function.

  The sparse representation of a matrix is a dictionary of keys, where each key
  is a tuple `(i, j)` and each value is the value found at position `i, j` in 
  that matrix. If the value at position `i, j` in the matrix is zero, it isn't 
  included in the dictionary.

# [Hint_5]

  After transforming the input matrices into their sparse representations, as
  mentioned in Hint #4, you can check if a particular element is non-zero before
  performing multiplications with it for various dot products, thereby reducing
  the number of operations performed by your function.
