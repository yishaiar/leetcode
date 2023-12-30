'''
Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

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

        self.assertEqual(solution(self,10),
                         False)

from typing import List
import unittest
# Solution
        


class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        orig,new = x,0
        while x>0:#transvers number, skip if x==0
            new = new*10 +x%10
            x = x//10
        return orig==new 
            


        

        

  
if __name__ == "__main__":
    unittest.main()