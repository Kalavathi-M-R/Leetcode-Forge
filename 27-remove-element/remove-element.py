class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for x in nums:
            if x!=val:   #use to skip the value, instead of removing it as it takes more memory
                nums[k]=x
                k+=1
        return k