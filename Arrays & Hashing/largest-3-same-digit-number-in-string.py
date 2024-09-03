class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left = 0
        right = 3
        largest = -1
        while right <= len(num): 
            number = num[left:right]
            if number.count(number[0]) == 3:
                if int(number) > int(largest): 
                    largest = number
            left += 1
            right += 1
        if largest == -1: 
            return ""
        else: 
            return largest
        
# This problem asks to return the largest 3-same-digit number in a string of numbers (Ex: 333 or 999) and so 
# what we had to do was to just find a way to compare three digits of the string at a time and then move that
# window across as we update the largest value accordingly. All I did was have a right and left counter, 
# loop until our right counter reached the end and only checked if the value was the greatest that we have seen so
# far, once we get to the end we should have the result. Also, since the integers are never negative, we can set largest
# to a negative number to check at the end if we ever found one 3-same-digit-number in the string.