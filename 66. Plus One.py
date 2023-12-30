'''
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. The large integer does not 
contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

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

        # self.assertEqual(solution(self,[4,3,2,1]),
        #                  [4,3,2,2])
        self.assertEqual(solution(self,[8,9,9,9]),
                    [9,0,0,0])

from typing import List
import unittest
# Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n-1]+=1
        while digits[n-1]>9:
                digits = digits if n-2>=0 else [0] + digits
                n = n if n-2>=0 else n + 1
                digits[n-1] = 0
                digits[n-2] +=1
                n -= 1            
        return digits
    


        

  
if __name__ == "__main__":
    unittest.main()