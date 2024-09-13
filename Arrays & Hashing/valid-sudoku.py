class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        collectRows = defaultdict(set)
        collectCols = defaultdict(set)
        collectNine = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".": 
                    continue
                elif(val in collectRows[i] or
                     val in collectCols[j] or 
                     val in collectNine[((i//3) * 3) + j//3]): 

                     return False
                collectRows[i].add(val)
                collectCols[j].add(val)
                collectNine[((i//3) * 3) + j//3].add(val)
        return True
    
# This problem gives us a sudoku board in the form of a 2D array and the empty spaces are represented by "." . 
# And our job is to find our whether or not the board at its current state is a valid sudoku board or not. So the way 
# to do this is to just check if each column and row have reapeating numbers which was the easy part. The hard part 
# was to figure out how to determine which 3 x 3 square the number we are looking at belongs to. So the way i did it 
# was to basically manipulate the indicies with math where a certain index of i + j will tell me which square we were in.
# To do this all i did was integer divided the x index by 3 and then multiplied it by 3, this will let me know which row of 
# 3 x 3 squares it belongs to. Then all we need to do is put them into dictionaries of sets, and check if the current value 
# that we are looking at are already inside the column, row or the 3 x 3 square. if it is then we return false.