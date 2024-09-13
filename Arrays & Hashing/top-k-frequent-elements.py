class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        intCount = Counter(nums)
        
        srt = sorted(intCount.items(), key = lambda item :item[1], reverse=True)
        print(srt)
        answer = []
        for i in range(k):
            answer.append(srt[i][0])
        return answer


# for this question, it asks us to find the k most frequent element inside a list. meaning if a list is like: 
# [1,1,1,2,2,3] and the k is 2 then we need to return the top 2 most frequent elements in our list. So to do this 
# i created a dictionary that had the key as the element and the frequency as the value to that pair. This way I 
# can do a sort based on the values of each key-value pair and insert these key value pairs into a list making it a 
# list of tuples. This way all that is left to do is to loop k times through this array and append the numbers into 
# a result list. Then we have the answer. The interesting thing that i learned from this question were lambda functions
# they are essentally functions that are not named and used only in whatever the context is. so in this case, in the sorted
# function, the second parameter key, takes in any function used to determine what we are basing our sort on. And so by creating 
# a simple lambda function that returns the value of the key-value pair, we can have our sorting function sort based on the 
# value of each pair. 