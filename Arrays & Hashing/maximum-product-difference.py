class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mini = min(nums) 
        nums.remove(mini)
        minProd = mini * min(nums)
        maxi = max(nums) 
        nums.remove(maxi)
        maxProd = maxi * max(nums) 

        return maxProd - minProd
    
    
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_big = second_big = 0
        first_small = second_small = float("inf")

        for n in nums:
            if n < first_small:
                second_small, first_small = first_small, n                
            elif n < second_small:                
                second_small = n                

            if n > first_big:
                second_big, first_big = first_big, n
            elif n > second_big:
                second_big = n        

        return first_big * second_big - first_small * second_small
    
    

# for this question, it asks us to find the maximum product difference between 4 numbers in a list. The product difference 
# between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d). And so the idea is to realize that this will be the 
# biggest when we find the difference between the product of the two smallest numbers with the product of the two largest numbers
# and so that is exactly what I did. The first solution takes advantage of the built in functions in python and the second solution 
# is a more general/ logical answer than can be done in any languauge.