#User function Template for python3
#https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/0
class Solution:
    def findMin(self, arr):
        #complete the function here
        n= len(arr)
        lo = 0
        hi = n-1
        while lo < hi :
            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                # Otherwise, the right side is sorted, so the
                # minimum must be in the left half (or be mid itself).
                hi = mid
        return arr[lo]