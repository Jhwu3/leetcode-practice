class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        pairs = defaultdict(int)
        for val in nums: 
            pairs[val] += 1
        
        for value in pairs.values(): 
            if value > 1: 
                total += ((value * (value-1))//2)
        return total
        
# this problem asks use to find the number of good pairs that can be made with a give list of integers
# a good pair is just two numbers that are equal but also in different indicies. And so they way I though of doing
# this was to find the number of times each integer showed up in the list. There I just used the algoritm 
# for the number of combinations n(n-1) / 2. Once we do that on each number that can for atleast one pair, 
# we have our answer.