class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0] > nums2[-1] or nums1[-1] < nums2[0]:
            return -1

        mp = defaultdict(int)

        for num in nums1:
            mp[num] = 1
        
        for num in nums2:
            if mp[num] == 1:
                return num
        
        return -1