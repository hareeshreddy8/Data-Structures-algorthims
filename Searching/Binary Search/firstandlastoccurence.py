class Solution:
    #problem link https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/0
    def find(self, arr, x):
        first = self.first_occurence(arr,x)
        last = self.last_occurence(arr,x)
        return [first,last]
    #method for first occurence
    def first_occurence(self,arr,x) :
        #initalising lo and hi 
        lo = 0 
        hi = len(arr) - 1
        #let first occurence be -1
        first = -1
        while lo <= hi:
            mid = lo + (hi- lo) // 2
            if arr[mid] == x :
                first = mid
                hi = mid-1
            #if arr[mid] is less than x
            elif arr[mid] < x :
            #check on the right side of arr 
                lo = mid + 1
            #else 
            else :
                hi = mid - 1
            
        return first 
    #method for last occurence 
    def last_occurence (self,arr,x):
        lo = 0 
        hi = len(arr) - 1
        #let first occurence be -1
        last = -1
        while lo <= hi:
            mid = lo + (hi- lo) // 2
            if arr[mid] == x :
                last = mid
                lo  = mid+1
            #if arr[mid] is less than x
            elif arr[mid] < x :
            #check on the right side of arr 
                lo = mid + 1
            #else 
            else :
                hi = mid - 1
            
        return last 