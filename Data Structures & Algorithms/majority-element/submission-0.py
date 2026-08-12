class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num] += 1
        
        for key in dictionary:
            if dictionary[key] >= len(nums) / 2:
                return key
            
        