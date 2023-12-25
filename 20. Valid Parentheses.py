'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

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

        self.assertEqual(solution(self,"Hello World"),
                         5)

from typing import List
import unittest
# Solution

class Solution:
    def isValid(self, s: str) -> bool:
        brackets= {'}':'{', ']':'[', ')':'('}
        stack = []
        for val in s:
            if val in brackets.values():#opening bracket - store in stack
                stack.append(val)
            #closing bracket and there's an opening bracket in stack which matchies the opening bracket
            elif val in brackets.keys() and len(stack) > 0 and stack.pop() == brackets[val]:                    
                continue
                # a = None
            else:
                return False 

        return True if len(stack) == 0 else False #if stack is empty, all brackets matched

        

  
if __name__ == "__main__":
    unittest.main()