class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        result = -1
        for i in range(len(nums)):
            right -= nums[i]
            if(left == right): 
                result = i
                break
            left += nums[i]
        return result
    
# This problem asks to find the pivot index of a list of integers which essentaill means at this index,
# the left side and the right side of the list add up to the same amount. So my solution is to find the
# total of the entire list, then loop through the list once, and checking if there is ever a index that 
# makes both sides equal by subtracting our current index from the right side and adding it to the left.
# Then we just need to return this index if found.