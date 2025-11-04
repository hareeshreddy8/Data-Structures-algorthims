#https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
class Solution:
    def checkEqual(self, a, b) -> bool:
        #let us keep count of key and values 
        freq_a = {}
        freq_b = {}
        #add keys,and values of list a 
        for num in a :
            freq_a[num] = freq_a.get(num,0) + 1
         #add keys,and values of list b
        for num in b:
            freq_b[num] = freq_b.get(num,0) + 1
        
        #check whether the dicts are same 
        return freq_a == freq_b
        