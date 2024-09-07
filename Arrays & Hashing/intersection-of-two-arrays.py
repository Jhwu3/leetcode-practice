class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)
        for val in nums1: 
            dic[val] = 1
        ans = []
        for val in nums2: 
            if val in dic: 
                ans.append(val)
                del dic[val]
    
        return ans

# this problem asks to find the intersection between two arrays, one super easy way to do this is to just convert both lists
# into sets and then find the intersection with the built in method of intersection in python. However, when i did this the 
# memory usage was very high since we are creating two sets. So a better way is to just use a dictionary, insert each number
# from one of the list into the dictionary and then loop through the other list and compare. The trick is to remove the number 
# from the dictionary after we find an intersection since this number can occur again in our second list. So once that is done, 
# we just return the list with the answer.