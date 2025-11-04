#https://www.geeksforgeeks.org/problems/check-for-disjoint-sets-or-arrays/1
class Solution:
    # Function to check if two arrays are disjoint
    def areDisjoint(self, a, b):
        freq_a = {}
        for num in a:
            freq_a[num] = freq_a.get(num,0) + 1
        #checking whether the elemnts in b have the same count as elemnts in a
        for num in b :
            if num in freq_a:
                return False
        return True