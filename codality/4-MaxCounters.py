'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

class Solution { public int[] solution(int N, int[] A); }

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
'''

# https://app.codility.com/demo/results/trainingJB5RNV-UMC/

def solution(N,A):
    # if len(A)==1 and N not in A: #empty array return 1 : min(2)>1->return 1
    #     return [1]
    # elif len(A)<2:
    #     return [0]
    n = len(A)
    MAX = max(A)
    # MIN = min(A)
    # if N+1 in A:
    count = [0] * (MAX)#exclude N+1 i.e MAX-MIN+1-1
    # else:
    #     count = [0] * (MAX)
    # past_count = [0] * N 
    # new_count = [0] * N
    
    N_in_A = False
    max_count = 0
    for k in range(n):
        if A[k]==N+1:
            N_in_A = True
            count = [max_count] * (MAX)
        else:
            count[A[k]-1] += 1#exclude 0 value
            max_count = max(max_count,count[A[k]-1])
    if N_in_A: return count[:-1]
    else: return count
    # return count         




import unittest
class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution(5,[ 3,4,4,6,1,4,4  ]),[3, 2, 2, 4, 2])
        self.assertEqual(solution(6,[ 3,4,4,6,1,4,4  ]),[1, 0, 1, 4, 0, 1])
        self.assertEqual(solution(3,[ 4  ]),[0,0,0])
        self.assertEqual(solution(4,[ 3  ]),[0,0,1])
        


if __name__ == "__main__":
    # A = [6, 4, 4, 6]
    unittest.main()
