class Solution(object):
    def removeDuplicates(self, nums):
        ret = []
        for i in range(len(nums)):
            if(nums[i] not in ret):
                ret.append(nums[i])
        nums[:] = ret
        return(len(ret))
