"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        lst = []
        count = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                lst.append(count)
                count = 0
            if i == len(nums) -1:
                lst.append(count)
            i += 1
        return max(lst)
