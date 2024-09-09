class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums= sorted(nums)
        prevVal = 0 
        length = len(nums)
        for i in range(length): 
            if nums[i] >= (length - i) and prevVal < (length - i ):
                return length - i
            prevVal = nums[i] 
        return -1

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0 for i in range(len(nums) + 1)]
        for val in nums: 
            index = min(val,len(nums))
            count[index] += 1
        total = 0 
        for i in range(len(nums), -1, -1):
            total += count[i]
            if i == total: 
                return i 
        return -1
    
# This question asks to find out if the given array is special. This means that there is a number x, such that
# there are exactly x numbers in the array greater than or equal to x. And this does not need to be an element in 
# the list. So to solve this problem we needed to figure out that our number x can only be in the range (1, n) 
# where n is the length of the list. So one way to do this is to sort the list, and just check for each index,
# if that index satisfy the special array qualifications. One edge case for that solution was to check if the previous
# value that we checked was equal to our current index. This can sometimes happen because if we dont include this,
# the solution wil indicate that we have a special number when we actually dont. A better way to do this problem is to recognize
# that we actually dont need to sore the list at all. we just need to go through the list, and count how many numbers 
# are greater than each number in the range of (1,n). This is because for example once we have the count of numbers greater than 5,
# when we do the calculations for 4, we just need to add the number of numbers greater than 4, which is a super set of the numbers 
# greater than 5 + the number of numbers equal to 4. This way, by going backwards to calculate the total, we dont need to sort the list
# and test if we have a special array or not. 