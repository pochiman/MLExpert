

from math import pow, sqrt

class Metrics():
    def euclidean_distance(self, X, Y):
        return sqrt(sum(pow(x - y, 2) for x, y in zip(X, Y)))
 
    def manhattan_distance(self, X, Y):
        return sum(abs(x - y) for x, y in zip(X, Y))
 
    def cosine_similarity(self, X, Y):
        numerator = sum(x * y for x, y in zip(X, Y))
        denominator = sqrt(sum([x * x for x in X])) * sqrt(sum([y * y for y in Y]))
        return numerator / float(denominator)
 
    def jaccard_similarity(self, X, Y):
        intersection_cardinality = len(set.intersection(*[set(X), set(Y)]))
        union_cardinality = len(set.union(*[set(X), set(Y)]))
        return intersection_cardinality / float(union_cardinality)


def distances_and_similarities(X, Y):
    similarity = Metrics()
    return [similarity.euclidean_distance(X, Y),
            similarity.manhattan_distance(X, Y),
            similarity.cosine_similarity(X, Y),
            similarity.jaccard_similarity(X, Y)]
