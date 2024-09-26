class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = math.inf
        topSum = sum(grid[0])
        bottomSum = 0

        for i in range(n):
            topSum -= grid[0][i]
            ans = min(ans, max(topSum, bottomSum))
            bottomSum += grid[1][i]

        return ans

# This problem gives us a list of dimensions 2 * n, essentially just two rows with a lenght of n as our board. 
# we want to find out in a game where two probots play, the maximum points the second robot can achieve. So to start,
# the first robot will travel in a way to minimize the total number of points the second robot can get. Each index of 
# the lists have a number on them and the total points is just the path traveled. The twist is that after robot 1 plays,
# the path that the first robot takes will be all 0, so the question asks to find the most points robot 2 can get while 
# robot 1 is trying to minimize the points robot 2 can get overall since it plays first. this can be done using prefix sums
# because since there are only two rows, whatever path robot 1 takes will leave either 1 or 2 sections with points, depending 
# on what path it took, but in any case, robot 2 will only be able to get the points from one of the two sections since, the
# robots can only move right or down. Once it moves down it can't move down again and it cant move up. So it can only collect 
# one of the two sections. Then we just need to use prefix sums on the two and bottom row and find the max between the top and 
# bottom row whhile also finding the overall minimum since robot 1 plays first.
