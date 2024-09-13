class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [] 
        pre = 1
        post = 1
        postfix = []
        for val in nums:
            prefix.append(pre)
            pre *= val

        for i in range(len(nums) - 1 , -1 , -1): 
            postfix.insert(0,post)
            post *= nums[i]
        answer = []
        for i in range(len(prefix)):
            answer.append(prefix[i] * postfix[i])
        return answer 
    
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1 
        postfix = 1
        for i in range(len(nums)): 
            answer[i] *= prefix 
            prefix *= nums[i]
            answer[len(nums)- 1 - i] *= postfix
            postfix *= nums[len(nums)- 1 - i]
        return answer
    

# This problem gives us a list of integers and asks us to return a list such that the answer[i] is equal to the 
# product of all the elements except the element in the given list's ith index. So to do this, it took me some time 
# to recognize that to get the product of all values except itself, we need to find the product of the values on the 
# left and the product of values on the right. And i originally created two different lists that contained the products 
# of each element's left and right values. While this worked, I did end up using three total lists to get the result. 
# i then learned that since we are doing multiplication, the order in which we are multiplying to get to the final product 
# did not matter, so now in one loop we just have two variables store the product of the right and the product of the left 
# of the elements we have seen so far. and by the end after we shifter the both prefix and postfix pointers across the list, 
# we will still end up with the same result.