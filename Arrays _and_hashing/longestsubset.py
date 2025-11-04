#https://www.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1
class Solution:
	def longestSubarrayDivK(self, arr, k):
        #creating hashmap to store occurences of remainders of prefix sum
        remainder_index = {}
            #output to be given is maxlength of subaray 
        max_len = 0
        prefix_sum = 0
        for i in range(len(arr)) :
            prefix_sum += arr[i] 
            remainder = prefix_sum % k 
            
            #if there are negative elements then remainder also will be neagative 
            if remainder < 0 :
                remainder += k
            #what if remainder is zero 
            if remainder == 0 :
                #them max length of sub array will be next to that index 
                max_len = i + 1
            #if remainder is there in remainder_index then the difference betwwn  index+1 and current index should me max_len
            elif remainder in remainder_index :
                length = i - remainder_index[remainder]
                max_len = max(max_len,length)
            #if the remainder is new store it as first occurence 
            else :
                remainder_index[remainder] = i
        
        return max_len