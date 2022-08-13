class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(len(nums)):
            if nums.count(nums[index]) > 1:
                del nums[nums.index(nums[index])]
            else:
                index += 1
        return len(nums) 
