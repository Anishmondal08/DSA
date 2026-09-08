class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr=[]
        brr=[]
        for i in range (len(nums)):
            if (nums[i]%2==0):
                arr.append(nums[i])
        for j in range (len(nums)):
            if (nums[j]%2!=0):
                brr.append(nums[j])
        crr=arr+brr        

        return crr        

        