class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}
        temp = list(t)
        for i in range(len(s)):
            if temp[i] not in seen:
                if s[i] not in seen.values():
                    seen[temp[i]] = s[i]
                    temp[i] = s[i]
                elif s[i] in seen.values() and temp[i] == s[i]:
                    return False
            else:
                temp[i] = seen[temp[i]]
        temp = "".join(temp)
        return temp == s

# this problem asks us to find out if the two strings are isomorphic, meaning by mapping the characters in one of the string to 
# the other strings characters. The reason why this was a bit difficult was because no two characters may map to the same character.
# And so my solution was to have a hashmap of what we seen that records all the mappings we have done so far. Then if we encounter 
# a different letter that wants to map to a character that already exists in the hashmaps values, we do one last check to see if our 
# current character is the same as the one we are trying to map to. this can't happen in the case that we already have this character 
# inside our hashmap's values. This would result in a Return value of false. But essentially we are just trying to actually map the second
# string to the first one. so when we return we just compare our temp string to the given one and see if they are equal.
