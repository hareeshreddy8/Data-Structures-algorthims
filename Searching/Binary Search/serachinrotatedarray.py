#https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/0
class Solution:
    def binarysearch(self,arr,lo,hi,x):
        while lo<=hi :
            mid = lo+(hi - lo)//2
            #left side is sorted 
            if arr[mid] == x:
                return mid 
            if arr[mid] < x :
                lo = mid +1
            else : 
                hi = mid -1
        return -1
    def findpivot(self,arr,lo,hi):
        #pivotis the minimum element in the array 
        while lo<hi :
            mid = lo+(hi-lo) //2
            if arr[lo] <= arr[hi]:
                return lo
            if arr[mid] > arr[hi] :
                lo = mid +1
            else :
                hi = mid
        return lo

    def search(self, arr, key):
        n = len(arr)
        pivot = self.findpivot(arr,0,n-1)
        if(arr[pivot] == key):
            return pivot
        if(pivot == 0):
            return self.binarysearch(arr,0,n-1,key)
        if(arr[0] <= key) :
            return self.binarysearch(arr,0,pivot-1,key)
        return self.binarysearch(arr,pivot + 1,n-1,key) 