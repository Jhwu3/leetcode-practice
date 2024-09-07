class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        longest = -1 
        for index, char in enumerate(s): 
            if char in seen: 
                longest = max((index - seen[char] - 1),longest)
            else: 
                seen[char] = index 
        return longest
        
# This question asks us to find the greatest distance between two characters that are equal. so to do this
# i created a dictionary to store what we have seen so far, and for the value of the pair we will store the 
# index of the character. then when we encounter the character again we will find the difference, and see if 
# that difference is bigger than what we have seen so far. Then just return the answer at the end.
