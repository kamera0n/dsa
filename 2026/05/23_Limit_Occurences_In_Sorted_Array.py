class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        # Why not just remove occurences of the list that occur more than k times? Note python does not like it when you change a list while you loop through it so we should use an external list
        # Loop through, to keep this O(N) because we know this is increasing we can have a current number and current count while we loop. If we're over the cap we simply stop adding current number
        res = []
        curr_num = 0
        curr_count = 0
        for num in nums:
            if num != curr_num:
                curr_num = num
                curr_count = 1
                res.append(num)
            elif curr_count == k:
                # If I was doing in place wouldn't I js delete here?
                continue
            else:
                curr_count += 1
                res.append(num)
        return res