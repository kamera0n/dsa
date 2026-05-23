class Solution:
    def check(self, nums: List[int]) -> bool:
        # The size of this problem space is pretty small, could I just rotate every elt and see if its sorted or is that TLE (this is O(N^2))
        # Given it has to have been sorted, couldn't I just take the smallest value, and then rotate it with that being first
        # The only thing that kind of hurts that is the fact there could be duplicates, so what is "smallest" 2, 3, 4, 2, this specific instance becomes even worse as there becomes more and more 2s in the problem
        # In a non-decreasing order the biggest duplicate would be the one preceeded by a bigger number (or the end), the smalllest would be preceeded by a smaller number (or the beginning). But in 2,3,4,2 the last 2 is acc the smallest one
        # Could I just rotate and then only check if a min value is first?
        #min_num = min(nums)

        # rotate left
        # 1,2,3,4,5 -> 2,3,4,5,1
        # just store first val and move everything up 1
        def rotate_left(arr):
            first_elt = arr[0]
            for i in range(len(arr) - 1):
                arr[i] = arr[i + 1]
            arr[-1] = first_elt

        # There's no way for me to tell the difference between shifted once and fully sorted so we check first
        if nums == sorted(nums):
            return True
        # What if we tried to find where the break is and rotate there?
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                break
            count += 1
        
        # Now we're going to rotate our list count times, in place(?)
        for i in range(count):
            rotate_left(nums)

        if nums == sorted(nums):
            return True 
        else:
            return False
        # Would it make sense to take the numbers, build the sorted array and then try to match that one? That is a much tougher implementation imo
