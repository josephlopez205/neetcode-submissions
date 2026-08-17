class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_len = 0
        for num in hashset:
            if (num - 1) not in hashset:
                length = 1
                while (num + length) in hashset:
                    length += 1
                max_len = max(max_len, length)
        return max_len