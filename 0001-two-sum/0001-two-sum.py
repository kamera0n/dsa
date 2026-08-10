class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We want to store whether the diff exists, and if so it's index
        # We loop through and store num: index
        # diffs = dict(enumerate(nums))
        diffs = {}
        for i in range(len(nums)):
            diffs[nums[i]] = i 

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffs:
                if i == diffs[diff]:
                    continue
                return [i, diffs[diff]]
        
        return []