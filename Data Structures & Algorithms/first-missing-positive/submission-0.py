class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for key, value in enumerate(nums):
            if value <= 0 or value > length:
                nums[key] = length + 1
         
        for value in nums:
            target_val = abs(value)
            if 1 <= target_val <= length:
                target_idx = target_val - 1
                nums[target_idx] = -abs(nums[target_idx])
        
        for index, num in enumerate(nums):
            if num > 0:
                return index + 1
        
        return length + 1