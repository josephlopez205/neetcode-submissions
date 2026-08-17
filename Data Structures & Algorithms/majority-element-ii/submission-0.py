class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_threshold = len(nums) / 3
        hashmap = dict(Counter(nums))
        res = []
        print(hashmap)
        for key, value in hashmap.items():
            if value > majority_threshold:
                res.append(key)
        return res
        