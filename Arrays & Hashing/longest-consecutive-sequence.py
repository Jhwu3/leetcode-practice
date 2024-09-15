class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0 
        seq = set(nums)
        for val in seq: 
            if val - 1 not in seq: 
                len = 0
                while (val + len) in seq: 
                    len += 1
                if len > answer: 
                    answer = len

        return answer 
    
# This problem asks us to find the longest consecutive elements sequence in a given list. So to do this, I used a set
# and use a loop through the list the find the start of a sequence. This means that I am just looking to find a number 
# without any number less than it in the list, then as long as the next element exist in the list we add to the sequence 
# length and then return the answer.