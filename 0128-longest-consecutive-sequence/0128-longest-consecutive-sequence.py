class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums) # O(n)
        count = 0
        nums = list(set(nums))
        for i in range(len(nums)):
            if nums[i] - 1 in check:
                continue
            n = nums[i]
            length = 1
            while (n + 1) in check:
                length += 1
                n += 1
            count = max(count, length)
        return count