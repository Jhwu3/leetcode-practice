class Solution:
    def maxProduct(self, s: str) -> int:
        n, pali = len(s), {} # bitmask : length 
        for mask in range(1, 1 << n): # 1 << n == 2 ** n
            subseq = ""
            for i in range(n): 
                if mask & (1 << i): 
                    subseq += s[n - i - 1]
            if subseq == subseq[::-1]: 
                pali[mask] = len(subseq) 
        result = 0
        for mask1 in pali: 
            for mask2 in pali: 
                if mask1 & mask2 == 0: 
                    result = max(result, (pali[mask1] * pali[mask2]))
        return result

         
# This problem is was very difficult for me to even think about how to brute force it. Essentially it asks us to find 
# the product of the length of the two longest palindromes in a given string which also having them being disjoint. This 
# just means that onces a letter is used in one of hhe subsequences, it cant be used in the other. The solution I came to 
# learn about was the usage of bit masks and bits to indicate wheter we select a letter or not. by having a bit representation 
# of the string, we are essentially indicating that we will pick a specific letter by making the position of that string, in 
# the bit number, 1. so an example would be: 
    
#     - the string "abcd" would be represented by a bit number of the same length. So 0000 in this case.
#     - then when we want to select a and c in our subsequence it would be 1010. 
#     - by comparing two different bit numbers using the & bit operator, we can see if any letters that we picked will conflict 
#         - this is because if we used the same letter in the two sequences, if we used the bit wise & on them, those positions will 
#           show up as a 1. 
#         - meaning if we use & and we get a 0 we have no collisions. 
# Then, to check every single combination of the letters, we just loop from 1 to 2^n where n is the length of the string. By using the
# bit representation of the numbers we can check every combination. then all we need to do is add those letters that we selected into a 
# string and check if the reverse is equal to find palidromes. if they are we will enter them into our dictionary that stores the bit mask 
# and the length of the subsequence as the key value pairs. then we just need to do a double loop into the dictionary to find: two bitmasks 
# that dont collide with the & operator once again and then finding the max product of all of those values that do not collide.