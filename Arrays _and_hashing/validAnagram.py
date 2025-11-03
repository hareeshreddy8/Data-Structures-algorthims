#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #counter function creates a dict to store {character:value}
        #ex:s = 'aab',t='abb' {a:2,b:1}=s,t={a:1,b:2}
        return Counter(s) == Counter(t)