'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''
from typing import List
import unittest

class Solution:
     def majorityElement(self, nums):
        n = len(nums)
        half = n/2
        count = {}
        for k in range(n):
            count[nums[k]] = count.get(nums[k],0) +1
            if count[nums[k]] > half:
                return nums[k]    
        return -1
        
class TestExercise(unittest.TestCase):
    """
    """
    
    def test_examples(self):
        # change function name to solution function name
        solution = Solution().majorityElement
        # nums1: List[int], m: int, nums2: List[int], n: int
        nums = [2,2,1,1,1,2,2]
        self.assertEqual(solution(nums),2)
        # self.assertEqual(solution([85,85],10,[85,85],30),3)

if __name__ == "__main__":

    unittest.main()