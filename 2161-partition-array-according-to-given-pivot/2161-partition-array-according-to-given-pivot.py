class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        pivot_count = nums.count(pivot)
        store = [0] * n
        i = 0

        for num in nums:
            if num < pivot:
                store[i] = num
                i += 1

        for _ in range(pivot_count):
            store[i] = pivot
            i += 1
        
        for num in nums:
            if num > pivot:
                store[i] = num
                i += 1

        return store