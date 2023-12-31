'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''
from typing import List
import unittest

class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = Solution().isPalindrome

        self.assertEqual(solution("A man, a plan, a canal: Panama"),True)
        self.assertEqual(solution("race a car"),False)
        self.assertEqual(solution(" "),True)


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = "".join(c for c in s if c.isalnum()).lower()
#         left,right = 0,len(s)-1
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left,right = left+1,right-1
    
#         return True
        
def two_pointers(s):
    left,right = 0,len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left,right = left+1,right-1
    
    return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        return two_pointers(s)

        
  
if __name__ == "__main__":
    unittest.main()