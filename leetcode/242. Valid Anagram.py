'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''
from typing import List
import unittest

class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = getattr(Solution,[func for func in dir(Solution) if callable(getattr(Solution, func))][-1])

        # solution = Solution().wordPattern

        self.assertEqual(solution(self, s = "anagram", t = "nagaram"),
                                            True)

from typing import List
import unittest
# Solution
def count_hashTable(input,count = {}):
    # from collections import OrderedDict
    # count = OrderedDict()
    for i in input:
        count[i] = count.get(i,0)+1
    return count

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = count_hashTable(s)
        t_freq = count_hashTable(t)
        if not  sorted(t_freq.keys()) == sorted(s_freq.keys()):#verify same keys in both
            return False
        for key in t_freq.keys():#verify number of occurance for each key 
            if t_freq[key] != s_freq[key]:
                return False     
        return True


  
        


        

  
if __name__ == "__main__":
    unittest.main()