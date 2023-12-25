'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

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

        self.assertEqual(solution(self,nums = [100,4,200,1,3,2]),
                         4)

from typing import List
import unittest
# Solution
def find_length(num,nums_set):
    max_length = 0
    while num in nums_set:
        num+=1
        max_length += 1
    return max_length

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums = list(nums_set)#without duplicates

        max_length = 0
        for num in nums:
            if num-1 in nums_set:#set is based on hash -O(1) complexity
                continue
            # check max length of serie from its first element
            max_length = max(max_length,find_length(num,nums_set))
        return max_length


            
            
        


        

  
if __name__ == "__main__":
    unittest.main()