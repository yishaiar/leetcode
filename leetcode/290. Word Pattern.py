'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

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

        self.assertEqual(solution(self,pattern = "abba", s = "dog cat cat dog"),
                         True)

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
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        pattern_freq = count_hashTable(pattern)
        s_freq = count_hashTable(s)
        if not sorted(pattern_freq.values())==sorted(s_freq.values()):#not same frequency
            return False
        # check exact locations - tranform pattern into s 
        s_keys = list(s_freq.keys())
        for i,key in enumerate(pattern_freq.keys()):
            pattern_freq[key] = s_keys[i]

        if s==[pattern_freq[letter] for letter in pattern]:
            return True
        return False


        

  
if __name__ == "__main__":
    unittest.main()