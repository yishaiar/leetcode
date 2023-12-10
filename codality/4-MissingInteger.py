'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) 
that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

# https://app.codility.com/demo/results/trainingQKXTRP-MHC/
    

        
def counting(A, m): #count for negative and positive values 
    n = len(A)
    count = [0] * (m + 1)
    MIN = min(A)
    for k in range(n):
        # i = (A[k]>0)*A[k] #exclude negative values4
        count[A[k]-MIN] += 1
    
    # dict= {}
    # for i in range(MIN,max(A)):
    #     dict[i] = count[i-MIN]    
    # print(dict)    
    return count
def solution(A):
    if len(A) == 0: #empty array return 1 : min(2)>1->return 1
        A = [2]
    
    MAX = max(A)
    MIN = min(A)
    if MIN > 1:
        return 1
    count = counting(A,MAX-MIN)
    for i in range(len(count)):
        
        if i+MIN <1:
            continue
        if count[i] == 0:
            return i+MIN
    return max(0,MAX)+1 # 0 if max is negative
    
    
import unittest
class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution([2, 3, 6, 4, 2, 2]),1)
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]),5)
        self.assertEqual(solution([-1, -3, -6, -4, -1, -2]),1)
        self.assertEqual(solution( [-1, -3, -6, -4, 1, -2]),2)
        self.assertEqual(solution([]),1)
        self.assertEqual(solution( [1]),2)
        self.assertEqual(solution( [2]),1)


if __name__ == "__main__":
    # A = [6, 4, 4, 6]
    unittest.main()
