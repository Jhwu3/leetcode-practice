class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = defaultdict(int) 
        for rect in rectangles: 
            ratio = rect[0] / rect[1]
            ratios[ratio] += 1
        total = 0
        for val in ratios.values():
            if val > 1:
                for i in range (1,val):
                    total += i 
        return total

# This question gives us a lists of lists, in which the smaller lists have two numbers, representing the 
# dimensions of the rectangle. It wants us to find the number of interchangable rectangles or in other case 
# rectangles that have the same width to length ratio. So to do this i created a dictionary of ratios, in which
# i tally up all the rectangle's ratios. Then all we need to do is loop through each ratio that has more than one 
# rectagle, then sum it up into a total. 
 