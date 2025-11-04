#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
     i , j = 0,len(numbers)-1
     while i < j :
        currsum = numbers[i] + numbers[j]
        if currsum > target :
            j -= 1
        if currsum < target :
            i += 1
        elif currsum == target :
            return [i+1,j+1]
     return [-1,-1]