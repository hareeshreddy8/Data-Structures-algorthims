class Solution:
    #https://www.geeksforgeeks.org/problems/count-1s-in-binary-array-1587115620/0
    def countOnes(self, arr):
        low = 0
        high = len(arr) - 1
        
        # This handles the "all zeros" case
        if arr[0] == 0:
            return 0
            
        # This handles the "all ones" case
        if arr[high] == 1:
            return len(arr)

        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == 1:
                # This is a 1. We need to check if it's the *last* 1.
                # It's the last 1 if the next element is 0.
                if arr[mid + 1] == 0:
                    # We found the boundary!
                    return mid + 1
                else:
                    # The next element is also 1.
                    # The last 1 must be to our right.
                    low = mid + 1
            
            else: # arr[mid] == 0
                # This is a 0. The last 1 must be to our left.
                high = mid - 1
                
        return 0 # Should be unreachable if array has 1s and 0s 