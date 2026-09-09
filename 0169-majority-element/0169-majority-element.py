class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=int(len(nums)/2)
    
        new=set(nums)
        for i in new:
            count=0
            for j in range (len(nums)):
                if nums[j]==i:
                    count+=1
                    if count>k:
                        return nums[j]
            

        