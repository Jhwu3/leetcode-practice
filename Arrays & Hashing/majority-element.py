class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        count = 0
        for num in nums: 
            if count == 0: 
                majority = num
            if num == majority: 
                count += 1
            else:
                count -= 1
        return majority

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums) // 2)]

# This question asked a simple question to find the element that occured more than n/2 times in the list 
# given that n is the length of the list. And so one way to do this was to sort the elements and then just 
# return the middle of the list, since one element is guarenteed to show up more than n/2 times, the middle 
# will for sure be that value. However, the additional challenge was to try and make the solution linear time 
# while also using O(1) space. I wasnt able to solve this and looked at other people's solutions. The solution
# to this was to have two integers keeping track of the numbers, majority and count. And so when count is 0,
# we set our majority as the current number that we are on. Then we just check if each number we loop upon 
# is equal to the majority number. if it is we add to the count and subract otherwise. This works because 
# since the majority will occur more than any other number, it will always have the actual majority integer
# as the number stored in our majority variable. Which is very clever (apparently called moore's voting algorithm)