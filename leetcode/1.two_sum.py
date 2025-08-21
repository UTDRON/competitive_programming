'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orig_idx = [{}]
        nums.sort()
        i, j = 0, len(nums)-1
        while i < len(nums) and j > -1:
            if nums[i] > target:
                return None
            if nums[j] > target:
                j -= 1
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
                continue
            else:
                j -= 1
                continue
        return None 


assert Solution().twoSum([3, 2, 4], 6) == [1, 2], "should be [1, 2]"
assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1], "should be [0, 1]"
assert Solution().twoSum([3, 3], 6) == [0, 1], "should be [0, 1]"