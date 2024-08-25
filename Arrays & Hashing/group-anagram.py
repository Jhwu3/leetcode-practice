class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} 
        result = [] 
        for i in range(len(strs)): 
            sword = ''.join(sorted(strs[i]))
            if sword not in seen: 
                seen[sword] = len(result)
                result.append([strs[i]])
            else:
                result[seen[sword]].append(strs[i])
        return result


# To solve this problem I created a dictionary that will store all the words that i have seen
# and a result list that contains my solution. And so the way I went about solving this was first 
# using the python function sorted() which is able to sort strings alphabetically. This way when I 
# sort the words if there were words that were anagrams, they would end up being the same string after 
# sorting them. This way I was able to compare the words with what i have seen so far. In my dictionary
# the key value pair that I am storing are the sorted word as the key and the index of where this group of 
# anagrams are in my result list as the value. and the way this worked was that evertime we ecounter a new
# anagram, we append it to the result list by getting the length of the list. If we have already seen it 
# then all we need to do is access the correct key-value pair in the dictonary and we can just append to 
# that index. 