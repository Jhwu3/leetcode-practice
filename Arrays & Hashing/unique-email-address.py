class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for mail in emails:
            temp = mail.split("@")
            if '+' in temp[0]: 
                subindex = temp[0].index('+')
                temp[0] = temp[0][:subindex]
            temp[0] = (temp[0].replace(".","")) + "@"
            seen.add("".join(temp))
        return len(seen)


# for this problem it asked us to find the number of unique email addresses in a given list of addresses. the twist was that 
# in an email's local name (Every valid email consists of a local name and a domain name, separated by the '@' sign.)
# there could be '.' characters and '+' characters. but whats important to note is that if periods exist in the local name
# it will be ignored and everything after the '+' character is ignored. and so what I did was first split each email by the
# "@" character which exists in every email. then we check if we have any '+' characters inside the local name. if we do,
# we update our local name to be the substring of just the stuff before the '+'. and then we just need to use the replace 
# method and replace all the '.' characters inside our local name. then I used a set to make sure the emails are unique 
# and just returned the length of that set.