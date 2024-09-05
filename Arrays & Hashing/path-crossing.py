class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}

        for direction in path:
            x += 1 if direction == 'E' else (-1 if direction == 'W' else 0)
            y += 1 if direction == 'N' else (-1 if direction == 'S' else 0)

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
    
# this problem asks us to determine whether a set of directions of north south east west, at any point 
# end up in a position that we have been on already. So all we need to do is to have variables to store 
# our locations and also a set so store all the locations we have been to, then we just need to check
# each move if we have been there or not and get the answer.