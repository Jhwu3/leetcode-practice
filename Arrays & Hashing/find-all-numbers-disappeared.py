class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lenn = len(nums)
        for i in range(lenn):
            val = abs(nums[i]) - 1
            nums[val] = abs(nums[val]) * -1
        res = []
        for i in range(lenn):
            if nums[i] > 0:
                res.append(i+1)
        return res


# this problem gives a list of length n and you are supposed to find which numbers in the range of n does not 
# show up in the list. and the extra constraint was to try to get it done with no extra space (aside from the answer) 
# and in O(n) time. Originally I created a set of the list and then looped from 1 to n and appended whichever numbers
# that were not inside the list. This works but does not satisfy the challenge of using no extra space. A clever solution
# that I learned was to manipulate the values in a way where we maintain the information given but we add a marker 
# to indicate that a number is in the list. And to do this for this problem, it was to make the numbers at the index negative
# if that number shows up in the list. 