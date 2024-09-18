class Solution:
    def maxArea(self, height: List[int]) -> int:
        greatest = 0 
        left = 0 
        right = len(height) - 1
        while left < right: 
            width = right - left 
            hght = min(height[left],height[right]) 
            water = width * hght 
            
            greatest = max(greatest,water)
            
            if (height[left] > height[right]): 
                right -= 1
            elif right > left: 
                left += 1
            else:
                left += 1
        return greatest
    
For this problem it asks us to find the most water that a container can store given a list of numbers 
that represent the height of the walls of the container. So to do this we need to set up two pointers on the 
right and left. and then check if the width multiplied by the lower of the two sides creates a larger volume 
that we have seen so far. Then after we check the whole list we return the answer.