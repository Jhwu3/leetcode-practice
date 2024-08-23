class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
            
            
# this problem asked to find the length of the last word in a string of words and 
# spaces. At first I was trying to do a while loop starting from the back of the string
# but there were cases where the string ends with a spacee. So my original idea of 
# just instantiating a count until we get to a space did not work out. so then I 
# remembered the .split() method for strings and was able to do it in one line