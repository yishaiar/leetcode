'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1

'''
from collections import deque# used for linked lists and stacks
from typing import List
import unittest

class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = getattr(Solution,[func for func in dir(Solution) if callable(getattr(Solution, func))][-1])

        # solution = Solution().wordPattern

        self.assertEqual(solution(self,3), 1)
        # self.assertEqual(solution(self,4), 2)
        self.assertEqual(solution(self,0),0)

from typing import List
import unittest
# Solution


class Solution:
    def mySqrt(self, x: int) -> int:
        # heron's method
        def epsilon(x,x0):
            delta = abs(x-x0*x0)
            return delta if delta==0 else delta/(2*x0)
        def floor(num):
            num1 = int(num)
            return num1 if num1<=num else num1-1


        x0 = float(x)/3#initial guess
        while (epsilon(x,x0)>1e-3):
            # print(x0)
            x0 = 0.5*(x0+x/x0)#iterative change of x0

        return floor(x0)
        
        

        

        

  
if __name__ == "__main__":
    unittest.main()