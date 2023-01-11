# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# #
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# #
# # You can return the answer in any order.
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

#Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hash_map:
                return [hash_map[dif], i]
            hash_map[n] = i