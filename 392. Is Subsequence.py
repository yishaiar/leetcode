'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
'''
from typing import List
import unittest





class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = Solution().isSubsequence

        self.assertEqual(solution("abc", "ahbgdc"),True)
        self.assertEqual(solution("axc", "ahbgdc"),False)
        self.assertEqual(solution("", "ahbgdc"),False)


from typing import List
import unittest

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False

        s_pos = 0#pointer for s in initial position
        for t_pos in range(len(t)): #pointer for t initial position is 0
            if s[s_pos] == t[t_pos]:
                s_pos += 1
            
            if s_pos == len(s): #found all chars of Subsequence
                return True
        
        return False #not found all chars in Subsequence
        
  
if __name__ == "__main__":
    unittest.main()