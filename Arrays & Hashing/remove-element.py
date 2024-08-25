class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num 
                count += 1
        return count 


# This problem was simple, it asks us to return the number of integers k, not equal to a given Value 
# but also remove (in-place) all the integers equal to the value while having the first k values in the
# list as those non equal values. So all you really had to do was loop through the list once, making sure 
# we have add one to the count whenever we encountered integers that were not equal, and also assigning the 
# nums[count] index in the list as the non equal value. 