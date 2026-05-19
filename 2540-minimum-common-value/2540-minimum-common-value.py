class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[-1] or nums1[-1] < nums2[0]:
            return -1
        
        if nums1[0] == nums2[0] or nums1[0] == nums2[-1]:
            return nums1[0]
            
        if nums1[-1] == nums2[0]:
            return nums2[0]
    
        store = set(nums1)

        for num in nums2:
            if num in store:
                return num
        
        return -1