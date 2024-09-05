class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        chrCount = defaultdict(int) 
        for word in words: 
            for c in word: 
                chrCount[c] += 1
        
        for c in chrCount: 
            if chrCount[c] % len(words) != 0: 
                return False
        return True
        
# This question asks gives us a list of strings and asks us to find out if through any number of operations, we can make 
# every string equal to each other. And one operation is defined as taking a character from one word and moving it into another
# word in any position. This question seemed complex to me and I was not able to solve it myself. In the end, I learned, that 
# by changing my way of thinking and realizing that the problem can basically be broken down to letter counting. This is because 
# for each word to be the same we need to use the same characters. So this problem became a lot easier after noticing that. 
# All we need to do after counting the total character counts is to see if for the length of our list, we have enough characters
# to distribute for each word.