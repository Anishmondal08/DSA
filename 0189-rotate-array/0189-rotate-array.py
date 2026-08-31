class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)

        first=nums[-k:]
        last=nums[:-k]
        
        nums[:]=first+last
        