#https://leetcode.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
      n =len(height)
      left = [0]*n
      right = [0]*n
      #left 
      left[0] = height[0]
      for i in range (1,n) :
        left[i] = max(left[i - 1],height[i])
      #right
      right[n-1] = height[n-1]
      for i in range (n-2,-1,-1) :
        right[i] = max(height[i],right[i+1])
      trappingwater = 0
      for i in range (0,n) :
        trappingwater += min(left[i],right[i])-height[i]
      return trappingwater