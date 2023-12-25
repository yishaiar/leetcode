'''
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

'''
from typing import List
import unittest

class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = Solution().canConstruct

        self.assertEqual(solution("aa",'aab'),True)

from typing import List
import unittest

def count_hashTable(input):
    count = {}
    for i in input:
        count[i] = count.get(i,0)+1
    return count
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        letters = count_hashTable(magazine)

        for i in ransomNote:
            letter_freq = letters.get(i)
            if letter_freq is None: #letter i not in letter
                return False
            elif letter_freq > 1:
                    letters[i] -= 1
            else:
                letters[i] = None
        return True

        

  
if __name__ == "__main__":
    unittest.main()