class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0 and ( i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n < 1: 
                        return True
        return n < 1
    
# this problem gives a list as a flower field where 1 repesents a planted flower and 0 represents an empty space.
# it asks for a given number n, if it was possible for the given flower field to plant n additional flowers given
# the condition that flowers cant be adjacent to eachother. And so the way I went about this was to first loop through 
# the list, check if our current index is 0, then check if the spots before and after are also 0, if this is the case,
# then we can plant a flower ( change the 0 to 1) then subtract from n. Then in any case n is less than 1, it means we 
# were able to plant the flowers in the flowerbed. One edge case were the two spots on the edges of the flowerbed 
# to account for this we can have or conditionals that in the case for the index to be the first or last element, we only 
# need to consider the immediate spot next to them for a flower to be planted there.