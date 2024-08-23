class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = len(nums)
        for i in range(x):
            nums.append(nums[i])
        return nums 
    
# 8/20/24  
# To solve this problem, it was very simple. Since it asks us for a list containing the 
# given list twice, we just need to loop through the list and append the contents to the 
# existing list. There were also better solutions including the .extend() method 
# which adds whatever you include in the extend method to the list that is calling it. So
# nums.extend(nums) will extend the content of the original list to itself.

        