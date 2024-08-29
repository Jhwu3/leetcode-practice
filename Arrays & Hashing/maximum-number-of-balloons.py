class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = text.count('l')
        o = text.count('o')
        n = text.count('n')
        return min(b,a,l//2,o//2,n)
        
        
# This problem was straightforward, it just asked to find how many times we can make the word
# balloon given a string and each character can only be used once. And so using the count method,
# we can just return the minimum of each letter count, to find the limiting character to make the 
# word balloon.