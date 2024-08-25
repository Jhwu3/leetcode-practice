class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            entry = [1] * i 
            row = len(result)
            for j in range(1,len(entry) - 1):
                entry[j] = result[row-1][j - 1] + result[row-1][j] 
            result.insert(i,entry)
        return result
    
# This problem took me quite some time because I was unable to translate the logic of Pascal's Triangle
# into code. At first I tried to use recursion but I was only able to come up with the base cases. I didn't 
# really know how to implement the recursive part properly. And so I settled with trying by creating each row 
# through a loop. by adding the previous row's values right above the row we are generating, I am able to 
# update each value properly.