class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen: 
                return[seen[diff], i]
            else:
                seen[nums[i]] = i
        
        return []

# For this very famous leetcode problem, it asks us to return the two indecies 
# that add up to a given target number. my solution was to have a hashmap that maps 
# the value of the index to the actual index. So it would look like  { "nums[i]: i" }
# where nums[i] is the value and i is the index. this way all I need to do now is loop 
# through the list once, check if the difference ( aka the other number needed to add 
# to the target ) exists in our dictionary. If it does then we can just return the answer
# and if it does not exist, we make our current value and index a new entry into the dictionary.
# And since the problem guarentees a solution, we will arrive at the answer with one loop.