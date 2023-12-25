'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P - 1] 
and A[P], A[P + 1], ..., A[N - 1].

The difference between the two parts is the value of: 
|(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 - 10| = 7
P = 2, difference = |4 - 9| = 5
P = 3, difference = |6 - 7| = 1
P = 4, difference = |10 - 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure 
'''

# def calcSum (A,p):
#     s1 = 0
#     s2 = 0
#     for i in range(p):
#         s1+=A[i]
#     for i in range(p,len(A)):
#         s2+=A[i]
#     return abs(s2-s1)

# def solution(A):
#     m=0 
#     for i in range(len(A)):
#         m += A[i]
#     # m = calcSum (A,1)
#     for p in range(2,len(A)):
#         m = min(m,calcSum (A,p))
#     return m
# https://app.codility.com/demo/results/trainingB76GYN-KF2/
def solution(A):
    # call sum of 2 parts of the array: left and right
    # sum(A) = left + right without importance of the specific p index
    # diffrence   = |(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])| =
    #             = |right - left| = |sum(A) - 2*left| = |sum(A) - 2*sum(A[:p-1]|
    #             = |sum(A) - 2*(A[p-1]+ sum(A[:p-2])|  
    
    s  = sum(A)
    if len(A)<2:
        return s
    # left = 0
    # min_diff = s
    left = A[0]
    min_diff = abs(s-2*left)
    if len(A)>2:
        for i in range(len(A)-2):
            left += A[i+1]
            min_diff = min(min_diff,abs(s-2*left))
    return min_diff
        
    
    
import unittest
class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution([]),0)
        self.assertEqual(solution([0]),0)
        self.assertEqual(solution( [1]),1)
        self.assertEqual(solution([3,1,2,4,3]),1)
        self.assertEqual(solution( [-3,-1,-2,-4,-3]),1)
        self.assertEqual(solution( [-3,1,-2,4,-3]),1)
        self.assertEqual(solution( [-10, -20, -30, -40, 100]),20)
        self.assertEqual(solution( [0,-200]),200)
        self.assertEqual(solution( [-100,200]),300)






if __name__ == "__main__":
    # A = [6, 4, 4, 6]
    unittest.main()
    

    
