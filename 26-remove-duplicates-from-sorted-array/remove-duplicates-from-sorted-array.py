class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        d = 1
        for i in range(len(nums)):
            if nums[i] != nums[d-1]:
                nums[d] = nums[i]
                d+=1
        return d


