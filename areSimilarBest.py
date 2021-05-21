def areSimilar(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2

A=[1,2,3,4,6,7,5]
B=[1,2,3,4,5,6,7]
print(areSimilar(A, B))