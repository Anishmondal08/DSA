class Solution(object):
    def intersect(self, nums1, nums2):
        result=[]
        for i in range (len(nums1)):
            for j in range (len(nums2)):
                if nums1[i]==nums2[j]:
                    result.append(nums1[i])
                    nums2.pop(j)
                    break
        return result            
        