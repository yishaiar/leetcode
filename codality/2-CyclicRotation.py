def solution(A,k):
    if len(A)>0:
        for i in range(k):
            # rotate once:
            A= [A[-1]]+A[:-1]
    return A


# https://app.codility.com/demo/results/training57P5UA-KMY/
A = [1,2,3,4]

print (f'{A}->{solution(A,k=4)}')