class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Couldn't I just combine, sort and then return the first one that returns twice?
        """res_list = list(set(nums1)) + list(set(nums2))
        res_list.sort()
        print(res_list)
        for i in range(len(res_list) - 1):
            if res_list[i] == res_list[i+1]:
                return res_list[i]
        return -1"""
        # Doesn't work because you can have dupes in one list and thus there's no way to know. Unless you set those lowk. Yeah this works, ugly asl tho
        # Also a good question for sets. Like couldn't I use a set difference and return the smallest element?
        return min(set(nums1).intersection(set(nums2)), default=-1)
        # Asked claude and they said yeah you could just 2 pointer which is fair. Glad I completed the challenge td tho! Test
