#https://www.geeksforgeeks.org/problems/array-pair-sum-divisibility-problem3257/1
class Solution:
    def canPair(self, arr, k):
        #array size should be even to get paired or else it leaves elemnts
        if len(arr) % 2 != 0 :
            return False
        #intiating dict to store remainder count of the elements
        rem_count = {}
        for num in arr :
            #store rem count in dict 
            rem = num % k 
            rem_count[rem] = rem_count.get(rem,0) + 1
        #so the dict is now stored with rems and their counts 
        #checking whether there is a remainder with 0 as value 
        
        if rem_count.get(0,0) % 2 != 0 :
                
            return False
        #checking if there is rem of value k/2 and it must be in a pair 
        if k%2 == 0 :
            half = k // 2
            #so to be in pair count of half rem sould be mod 2 
            if rem_count.get(half,0) % 2 != 0 :
                return False
        #pair up remaining rems using the condition r+k-r%2 == 0
        for r in rem_count :
        #must skip the iterations of rem that checked above 
            if r == 0 or (k // 2 == 0 and r == k // 2) :
                continue
            comp = k - r
            if rem_count.get(comp,0) != rem_count.get(r,0) :
                return False
        return True