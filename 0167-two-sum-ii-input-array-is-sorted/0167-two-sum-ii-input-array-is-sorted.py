class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=0
        l=len(numbers)-1
        while r<len(numbers):
            if numbers[r]+numbers[l]==target:
                return(r+1,l+1)
            elif numbers[r]+numbers[l]<target: 
                r+=1 
            else:
                l-=1      

        