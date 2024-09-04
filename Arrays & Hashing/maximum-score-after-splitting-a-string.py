class Solution:
    def maxScore(self, s: str) -> int: 
        if s[-1] == "1": 
            right = 1
        else:
            right = 0 
        s = s[:-1]
        left = s.count("0")
        total = left + right
        while len(s) > 1:
            val = s[-1] 
            if val == '1': 
                right += 1
            else: 
                left -= 1
            total = max(total, left + right)
            s = s[:-1]
        return total 

# this problem wants us to find the greatest score from splitting a string of 1 and 0's and The score after splitting a string
# is the number of zeros in the left substring plus the number of ones in the right substring. So to do this I started at the 
# end of the list, since the splits had to have atleast one value on each end, I checked the end value first. Then, after removing
# that from the list we check we just need to add 1 to the right if the number we are removing is a "1" or subtracting from the 
# left side if it is not the case. Then we just check for this instance of splitting if our score is greater than what we have seen
# before. Then at the end just return the largest score we found. 