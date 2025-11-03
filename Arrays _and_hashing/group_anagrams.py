#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = {}
        for word in strs :
            key = tuple(sorted(word))
            if key not in anagrams_group :
                anagrams_group[key] = []
            anagrams_group[key].append(word)
        return list(anagrams_group.values()) 