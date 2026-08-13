class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while True: 
            swaps = 0   
            for index, num in enumerate(nums):
                if index < len(nums) - 1:
                    if nums[index] > nums[index + 1]:
                        temp = nums[index]
                        nums[index] = nums[index + 1]
                        nums[index + 1] = temp
                        swaps += 1
                else:
                    break
            if swaps == 0:
                break