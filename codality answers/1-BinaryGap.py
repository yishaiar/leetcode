# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends
# in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. 
# The number 20 has binary representation 10100 and contains one binary gap of length 1. 
# The number 15 has binary representation 1111 and has no binary gaps. 
# The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. 
# The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap
# is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].
# Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

# https://app.codility.com/demo/results/trainingHTH328-ZER/
def to_binary(n):
    """
    """
    # print(bin(n))
    return bin(n)[2:]

def solution(n):
    n = list(to_binary(n))
    max_gap = 0
    counter = 0
    for i in n:   
        if i == '1':#start gap/close gap
            max_gap = max(max_gap,counter)
            counter=0
        else:
            counter+=1
    
    return  max_gap

# 9,529,15
# N = 1041
# print(f'{N}:{solution(N)}')



import unittest
class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution(1041),5)
        self.assertEqual(solution(32),0)
        self.assertEqual(solution( 529),4)
        self.assertEqual(solution(20),1)
        self.assertEqual(solution( 15),0)
        self.assertEqual(solution( 1),0)






if __name__ == "__main__":
    # A = [6, 4, 4, 6]
    unittest.main()
    # print(solution(1041))