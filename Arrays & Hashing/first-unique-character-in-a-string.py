class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, c in enumerate(s): 
            if c in seen: 
                seen[c].append(i)
            else:
                seen[c] = [i]
        
        for key, val in seen.items(): 
            if len(val) == 1:
                return seen[key].pop()
        return -1 
    
    
# for this problem it asks us to find the first unique character in a given string. To do this we use a dictionary 
# that has values as a list. I wanted to do it this way to store the characters that occurs more than once. This 
# way, when i look for the first unique character, since dictionaries are ordered, i can just loop throught the lists,
# and find the first list that has a length of 1. 
