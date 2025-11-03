#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        for i,num in enumerate (nums) :
            value = target - num
            if value in set :
                return [set[value],i]
            else :
                set[num] = i