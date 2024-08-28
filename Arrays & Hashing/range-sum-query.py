class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        total = 0 
        for val in nums: 
            total += val
            self.sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0: 
            return self.sums[right] - self.sums[left - 1] 
        else:
            return self.sums[right]
        
# for this problem, it asks us to construct a class NumArray that has the method sumRange that returns 
# the sum for two given indicies left and right. and so originally, i just had this function loop between 
# left and right and added up the numbers. But this solution had a really long runtime and so I came to this
# solution. I was not able to realize this on my own but basically how this works is that when the NumArray 
# is initialized, we create a list that basically stores sum at that particular index, what this means is that
# for example, at index 2 we will store the total of what came before 2 (including index 2) and with this list
# we are able to take the total that came before our left index and subtract that from our total at the right Index.
# this will then accurately give us the sum at the range left to right.