class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = len(nums)
        for i in range(x):
            nums.append(nums[i])
        return nums 

        