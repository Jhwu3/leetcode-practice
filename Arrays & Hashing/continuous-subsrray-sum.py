class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0
        for i in range(len(nums)): 
            total += nums[i]
            remain = total % k 
            if remain not in remainder: 
                remainder[remain] = i 
            elif i - remainder[remain] > 1:
                    return True 
        return False
    
# This problem gives us a list of integers and a number k. Our goal is to find out if any subarray of the list sums up 
# to the given number k or a multiple of k. The constraint was that the subarray had to be atleast length 2. My thinking 
# was to use a prefix sum and also calculate the remainder (divided by k) of that prefix sum at every index. The reason to do this was 
# that by finding the remainders of the sums when we encounter a remainder we have seen already, then it means we have added some 
# number to the sum that is a multiple of k. From there I could not figure out the edge cases but later learned that by also storing 
# the index of each remainder, we can just find the difference between the first time we seen this remainder and the second time,
# if this difference is more than 1, then it means we have a valid subarray. The last edge case was when find a remainder of 0. 
# Since this means the prefix sum it self is a multiple of k, we should naturally return true. However, in the case that this 
# only happened because we added some multiple of k in the very first value, then this is not valid, and we had to preemtively 
# enter 0 with the index of -1 to address ths edgecase so that when we find the difference we will get a number not greater than 1.