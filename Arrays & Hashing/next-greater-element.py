class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {} 
        for i, val in enumerate(nums1):
            dic[val] = i

        result = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            current = nums2[i]
            while stack and current > stack[-1]:
                temp = stack.pop() 
                result[dic[temp]] = current
            if current in nums1: 
                stack.append(current)
        return result


# For this problem, it asks to find the next greater element of some element x in an array is the first greater 
# element that is to the right of x in the same array. Essentally, given two arrays, you are supposed to find the 
# next greater element of every element of the first list, inside the second list. I know it is hard to explain with
# words so I will include an example below. (* the problem also mentions that the first list is a subset of the second.)

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# and so to solve this, one way is to loop through each value of the first list, find its index in the second list, 
# then do another loop starting from that index to the end of the second list and find the first value that is greater
# than our starting value. This is a O(n * m) solution given that n is the length of list1 and m is the length of list2.
# The Follow up to the question asks us to find a O(n + m) solution and from the solutions I learned a method known as 
# monotonic stacks. In this case this means that we use an additional dictionary to first store the key value pairs of
# value : index of each element inside list1. Then we use a stack to loop through the second list, we first check if the
# stack is empty and if our current element is greater than the top value of the stack. If it is greater we can just use our
# dictionary to map our current element to find the index that we need to update in our result list. And after that, we only 
# add this element on to our stack, if this element is even in our first list. This way the values in our stack are always 
# decreasing and therefore monotonic. 
