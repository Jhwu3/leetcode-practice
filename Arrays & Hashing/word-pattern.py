# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         lst = s.split()
#         count = 0
#         seen = {}
#         if len(lst) != len(pattern):
#             return False
#         for i in range(len(lst)):
#             if lst[i] not in seen:
#                 if pattern[count] not in seen.values():
#                     seen[lst[i]] = pattern[count]
#                 else:
#                     return False
#             lst[i] = seen[lst[i]]
#             count += 1 
#         return pattern == "".join(lst)
    
    
# this problem gives a pattern in lowercase letters like: "abba" and one non empty string and in this
# string words are separated by spaces like this: "dog cat cat dog" so what we need to do is check if 
# this string follows the same pattern as the given pattern by matching each of the words to a letter in 
# the pattern. To do this I used a dictionary to keep record of the mappings of words to pattern letter,
# we only add a new mapping if we havent seen this word and pattern letter ( making this a valid mapping). 
# And if it is a valid mapping, we change the word into the letter that it is equal to in terms of pattern letters.
# But if we see a new word trying to use a previously used pattern letter, we return false. And by the end, we 
# just need to compare the patter, the mapping that we made.