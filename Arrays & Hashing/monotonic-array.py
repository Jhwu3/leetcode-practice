class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] <= nums[-1]: 
            for i in range(1, len(nums)): 
                if nums[i-1] > nums[i]: 
                    return False
        else: 
            for i in range(1,len(nums)): 
                if nums[i-1] < nums[i]: 
                    return False
        return True
    
# For this problem, it asks us to find out if a list is monotonic, meaning if the integers are increasing in size,
# the integers that come after should all be increasing or the same. For decreasing integers it is the same. 
# Just that as long as it is decreasing or increasing, it should keep that pattern and stay that way. My solution 
# was to first check the values of the first and last integer in the list to determine if they are increasing 
# or decreasing, once we find the pattern, we just need to loop once, and check if this pattern is held out 
# through the list. 