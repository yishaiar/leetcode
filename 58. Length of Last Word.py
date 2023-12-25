'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring  consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''
from typing import List
import unittest

class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = Solution().lengthOfLastWord

        self.assertEqual(solution("Hello World"),5)
        self.assertEqual(solution("   fly me   to   the moon  "),4)
        self.assertEqual(solution("luffy is still joyboy"),6)
        # self.assertEqual(solution([85,85],10,[85,85],30),3)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in s.split()[::-1]:#split words and reverse
            return len(i)
        

            
        
        

if __name__ == "__main__":
    unittest.main()