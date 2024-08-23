class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start1 = 0
        start2 = 0 
        while (start2 < len(t)) and (start1 < len(s)):
            if(t[start2] == s[start1]):
                start1+= 1
            start2+= 1

        return start1 == len(s)
    
# This problem gives 2 strings s and t where your goal is to find whether s is a subsequence of t. 
# ( A subsequence of a string is a new string that is formed from the original string by deleting some 
#  (can be none) of the characters without disturbing the relative positions of the remaining characters.)
# My thinking was to have two pointers starting at the beginning of the strings and check each character 
# of t. since we are looking for subsequence, the order of the letters matter and so it is fine to move to 
# the rest of the characters if the current ones that we are examining do not match. Then at the end we just 
# need to check if our pointer for s has reached the end. If we didn't that means we do not have a subsequence.

