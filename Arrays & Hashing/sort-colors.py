class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0 , len(nums) - 1
        i = 0 
        while i <= right: 
            if nums[i] == 0: 
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2: 
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                i -= 1
            i += 1
            
# This question gives us a list of "color" which are just represented in three numbers 0, 1, and 2. This question 
# asks us to sort this list in place and also try to make it so we only use a one pass algorithm with constant extra space.
# To do this since we know the numbers can only be 0, 1, and 2, we can have two pointers starting at both ends of the list, 
# then have a index loop go through the list once. As we go through we just check if the element we are examining is 0 or 2. 
# If it is 0 then we move it to the front and shit out left pointer over by one. If it is 2 then we do the opposite. This way,
# the arry ends up being sorted without any extra passes and O(1) extra space.