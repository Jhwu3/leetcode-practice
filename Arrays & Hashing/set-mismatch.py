class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        allNums = [0 for _ in range(len(nums) + 1)]
        answer = [0,0]
        for num in nums:
            allNums[num] += 1

        for val in range(1, len(allNums)):
            if allNums[val] == 2: 
                answer[0] = val
            elif allNums[val] == 0: 
                answer[1] = val 

        return answer
    
# this problem asks us to find the number that is repeated in the list and also find out the number that we are missing 
# since the list is supposed to contain numbers 1 to n in a list of length n. so the way i thought of doing this was to 
# generate a list of length n + 1, then go through each number in the nums list and add 1 at the index of whatever number 
# we are on. Then we just need to loop through it once more to find which index has a value of 0 and which has a value of 
# 2. Then we just return that as a list.