class Codec:

    allchar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    def __init__(self): 
        self.urlToCode = {} 
        self.codeToURL = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.urlToCode:
            randCode = ''.join(random.choices(Codec.allchar, k=6))
            if randCode not in self.codeToURL:
                self.codeToURL[randCode] = longUrl
                self.urlToCode[longUrl] = randCode

        return "http://tinyurl.com/" + randCode 


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codeToURL[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# This question basically asks us to emulate the features of tinyurl which is a service that returns a shorter url 
# for any url that you provide. The question asks us to do the decode and encode where the proper links are acessed
# and also shortened. So to do this, i chose to have a string containing all the lowercase letters, uppercase letters 
# and number which i pick from randomly 6 times. 6 times is a good size because since there are total of 62 different 
# characters, we can have up to 62^6 different encodings which is more than enough. In any case, once generated our
# random code, we will then check if it already exists in our dictionary. If it does exist we need to generate a different
# code. This way it prevents any collision. So then all that is left to do is to properly enter the longurl and code into the 
# dictionaries, and we are able to easily decode just by doing a dictionary call.