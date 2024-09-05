class Solution:
    def minOperations(self, s: str) -> int:
        total = 0 
        for i in range(len(s)): 
            if i % 2 == 0: 
                if s[i] == '1': 
                    total += 1
            else: 
                if s[i] == '0': 
                    total += 1
        return min(total, len(s) - total)



# for this problem, it gives us a string consisting of 1 and 0. And it asks us to find the least number of changes
# required to make the string a string of alternating 0 and 1s. and so to do this i originally thought about looping
# through and checking whether or not the number that came before and after matched the alternating pattern. However, 
# this approach did not work out for some scenarios as doing this type of change does not always get the minimum number
# of changes required to alter the string into the alternating form. And so I learned that, because the order is always 0
# and 1 our pattern can only be in 1 of two ways. So now to do this we just need to find how many changes we need for us 
# to match one of the two patterns: (which is just "10101010..." or "01010101..."). Once we get the count we just need to 
# recognize that the two patterns are opposites of eachother. So the totals are opposites as wells, meaning the total to change 
# our string into one form, is the opposite of the total to change our string into the other form. So we just need to find the smaller
# between the two and return that result.