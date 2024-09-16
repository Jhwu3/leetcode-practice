class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGaps = defaultdict(int) 
        for row in wall:
            gap = 0 
            for i in range(len(row)-1):
                gap += row[i]  
                countGaps[gap] += 1
        if countGaps: 
            return len(wall) - max(countGaps.values())
        else: 
            return len(wall)
        
# This problem gives us a 2d array of numbers that represents bricks on a wall. The numbers represent the widths 
# of each brick but no matter what each row adds up to the same length since they make up a wall. The question asks
# us to find a vertical line down this wall where it cuts through the least amount of bricks. It is specified that 
# the edges of bricks dont count as cutting through them. So to do this you count the number of gaps (edge of two bricks)
# in each index position. Doing it this way makes it so we dont need to try out every possible position for a 
# line as we just need to find the index with the most number of gaps. then all we need to do is find how many total rows
# we have, then subtract the number of gaps and we will find the number of bricks we need to cross through. 