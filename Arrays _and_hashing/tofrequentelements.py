#https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pair = count.most_common(k)
        result = [element for element, count in pair]
        
        return result