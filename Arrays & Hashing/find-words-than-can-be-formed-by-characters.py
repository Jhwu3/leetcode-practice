class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        char_count = Counter(chars)
        
        for word in words:
            temp_count = char_count.copy()
            can_form_word = True
            for char in word:
                if temp_count[char] <= 0:
                    can_form_word = False
                    break
                temp_count[char] -= 1
            
            if can_form_word:
                result += len(word)
        
        return result
    
# this problem gives a string of characters and a list of words, and it asks us to find the total length of 
# words that can be made with the given characters. This was a little confusing to me because, I wasnt sure if
# this meant that once a character is used once for one word, we can't use it again. But upon further reading it 
# seemed like that was not the case and jsut asked if we can use the given characters to form each word. One thing
# I learned from this problem was the Counter method from python. This essentially creates a hashmap for us with 
# the claues of each pair as the number of times a character appears in the given string. So using that we did not 
# need to write out our loop to make a hahsmap. From there we just needed to decrement from the hashmap ever time 
# we encountered a character in each word. and only add to the total length if we can get to the end of the word, without 
# any characters in our hashmap going negative. 