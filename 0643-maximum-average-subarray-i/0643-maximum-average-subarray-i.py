class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_s=0
        for i in range (k):
            w_s+=nums[i]
        m_s=w_s
        left=0
        for right in range (k,len(nums)):
            w_s-=nums[left]
            left+=1
            w_s+=nums[right]

            m_s=max(w_s,m_s)
        return m_s/k        
        