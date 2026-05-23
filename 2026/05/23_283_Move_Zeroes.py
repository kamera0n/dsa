class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # Is this not just a question of how many of the zeroes in the array are not in the last few spots?
        # Couldn't we count the number of zeroes, z and then look at the last z numbers. If any of the last z numbers are not 0 then they need to be swapped so we return last z numbers minus non 0 last z numbers?
        res = 0
        # Zero Counter
        z = 0
        for num in nums:
            if not num:
                z += 1
        #print("z: ", z)
        # Non-z last number counter
        last_zs = 0
        for i in range(1, z + 1):
            #print("nums[-i]: ", nums[-i])
            if not nums[-i]:
                last_zs += 1
        #print("last_zs: ", last_zs)
        return z - last_zs
        # Maybe we two pointer this? One at the beginning and one at the end, we go until they hit each other©leetcode