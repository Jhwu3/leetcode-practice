class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1 
        for i in range(len(arr) - 1, -1, -1):
                temp = arr[i] 
                arr[i] = greatest
                greatest = max(greatest, temp)
        return arr 


# 8/20/24    
# This problem asks to return a list with each element representing the greatest element among 
# the numbers to its right. so the way I thought of doing this was to start from the end of the
# list then working my way back to the front. this way every time move towards the front, I can 
# keep track of the largest element we have seen so far. originally, I had the starting greatest
# number set to 0, which would then be updated as we scan the list. but this was not efficient since  
# I had to do a different manual check for the very last index of the list since it does not have 
# any elements to its right. Then from another solution, I learned that it was possible to just 
# set the starting greatest as -1 which made it so I did not have to do the manual check and made my 
# solution much simpler
        