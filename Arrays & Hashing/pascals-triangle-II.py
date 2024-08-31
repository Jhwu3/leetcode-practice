class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: 
            return [1]
        result = [1] 
        for i in range(1, rowIndex + 1): 
            result.append(int((result[i - 1] * (rowIndex + 1 - i))/i))
        return result

# This problem is an extension to pascal's triangle where it asks to return a specific row of pascals triangle 
# To solve this, I had to find out the formula for generating a row of pascals triangle. I leanred that to get 
# the next element on the row, we are essentially doing (previousValue * (n - k + 1))/k. To make it simple
# an example would be: for row index of 5, previousValue * (5 - 1 + 1)/ 1 is how we would get the second value of 
# the fifth row, and then each value following that, we are just incrementing k. then all we need to do is return 
# the list and we are done.