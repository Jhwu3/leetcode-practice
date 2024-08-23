class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        length = len(strs[0])
        while strs[0][:length] != strs[-1][:length]:
            length -= 1
        if length < 1:
            return ""
        return strs[0][:length]
    
# This problem asks us to return the longest common prefix amongst all the strings in the given list
# My first thought was to take the first word then using substrings to compare a substring of that first 
# word with the rest of the words using the same substring length. However my original idea was to start 
# with a substring length of 1, did not really work out with the cases where we did not have any common 
# prefix. One way I learned from other people's solutions were to go backwards and start with a substring 
# of the entire word, which would then be decreased as long as the substrings were not equal to eachother. 
# My approach was using the sorted python function which sorted strings alphabetically. this way, the list 
# would have the most different strings at the two ends. with this i can just do one loop until the first and the 
# last word have equal substrings. Then just check whether that length is 0 to return an empty string, if not then
# we return the common substring. 

# *** I am aware that this solution uses a sort meaning the runtime for my solution would be O(nlogn) instead of
# log(n) without sorting. I just thought since the problem constraints had a max list len of 200, it would be fine
# to use a sort function.