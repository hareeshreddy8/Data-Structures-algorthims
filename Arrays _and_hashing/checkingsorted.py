#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
class Solution:
    def check(self, nums: List[int]) -> bool:       
        peak_index = 0
        n = len(nums)
        for i in range (n) :
            if nums[i] > nums[(i+1) % n] :
                peak_index += 1
        return peak_index <= 1