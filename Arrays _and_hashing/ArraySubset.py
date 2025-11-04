#https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        #create a dict to keep count of elements in a 
        freq_a = {}
        for num in a:
            freq_a[num] = freq_a.get(num,0) + 1
        #checking whether the elemnts in b have the same count as elemnts in a
        for num in b :
            if num not in freq_a or freq_a[num] == 0 :
                return False
            freq_a[num] -= 1
        return True