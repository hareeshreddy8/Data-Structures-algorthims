#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        updated_list = set(nums)
        return len(updated_list) < len(nums)