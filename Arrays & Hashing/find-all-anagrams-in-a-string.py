class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        p = sorted(p)
        result = []
        for i in range(len(s) - n + 1):
            substr = sorted(s[i:i+n])
            if substr == p: 
                result.append(i)
        return result

# This questions asks to find the starting index of all the anangrams within a string according to another given 
# string. The solutiona above is done with brute force using sorts to match up the substrings. Essentially I just 
# want to each each substring of length p (where p is the given string to check) and find if we have a matching anagram.
# However I know there is a better solution. 