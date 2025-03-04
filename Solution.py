class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        if(val not in nums):
            return(len(nums))
        else:
            for i in range(len(nums)):
                if(nums[i] != val):
                    k += 1

            for i in range(len(nums) - k):
                nums.remove(val)

                
        return(k)
