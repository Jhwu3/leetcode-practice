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

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return [] 
        result = [] 
        pDict = defaultdict(int) 
        sDict = defaultdict(int)
        for i in range(len(p)):
            pDict[p[i]] += 1 
            sDict[s[i]] += 1
        
        if pDict == sDict: result = [0]
        left = 0
        for right in range(len(p), len(s)):
            sDict[s[left]] -= 1 
            if sDict[s[left]] == 0: 
                sDict.pop(s[left])
            sDict[s[right]] += 1 
            left += 1
            if pDict == sDict:
                 result.append(left)
        return(result)


# This solution uses a method called sliding window. What we need to do is populate one dictionary with the count of each letter in p, 
# then populating our substring dictionary to have the counts of the letters of the first len(p) characters. This way we initialize our 
# window to be in the beginning, and begin our first comparison for anagrams. This works because we can use == on two dictionaries and it 
# will return true if all key value pairs from each dictionary are equal. Then as we move our window along the string, we just need to remove 
# the very first character from the last check, and include the new character that encountered from the back. This way this makes each operation
# constant and allows for contstant space usage of at most 26 for each letter of the alphabet. In terms of time complexity, we loop through the 
# p string once and the s string once so it would be O(p + s) or to put it simply O(n) time complexity

# Space: O(1)
# Time: O(n)
         



        