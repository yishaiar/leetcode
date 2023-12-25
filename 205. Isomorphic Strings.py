'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a 
character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''
from typing import List
import unittest

class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = Solution().isIsomorphic

        self.assertEqual(solution(s = "bbbaaaba", t = "aaabbbba"),False)

from typing import List
import unittest

def count_hashTable(input):
    # from collections import OrderedDict
    # count = OrderedDict()
    count = {}
    for i in input:
        count[i] = count.get(i,0)+1
    return count
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        
        s_freq = count_hashTable(s)
        t_freq = count_hashTable(t)
        if not sorted(t_freq.values())==sorted(s_freq.values()):#not same frequency
            return False
        # check exact locations - tranform t into s 
        s_keys = list(s_freq.keys())
        for i,key in enumerate(t_freq.keys()):
            t_freq[key] = s_keys[i]

        if s==''.join([t_freq[letter] for letter in t]):
            return True
        return False

  
if __name__ == "__main__":
    unittest.main()