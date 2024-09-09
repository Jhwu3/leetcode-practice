class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0 
        for i in range(len(tickets)):
            if i <= k: 
                total += min(tickets[i], tickets[k])
            else: 
                total += min(tickets[i], tickets[k] - 1) 
        return total 
    
# This problem gives us a list of integers, where the length of the list represents the number of people who 
# are on line to purchase a ticket. the individual elements are how many tickets each person wants to buy and the 
# trick is that each person takes 1 second to purchase a ticket but then have to move to the back of the line. 
# So then given a specific index on hte list( or position of the line), how many total seconds will it take for that
# person to buy the ticket. And to solve this, we had to recognize the factor that decided how many total seconds each 
# person needed to buy their tickets. for people ahead of our person, since they will all take 1 second each time,
# until our person is done buying their tickets, they will continue buy tickets or until they had the amount that they needed. 
# And so this way we can see that the total time they will take is either the number of tickets they need or the number of tickets
# our individual needs(depending on which is smaller). and for the people behind our person, they get one less roatation because, 
# at the last line rotation, even if they have more tickets to by, we only need to count the total time for our individual, 
# not the people behind. And so that is one less rotation compared to our persons ticket amount, or whatever amount they need if that 
# amount is smaller. Then we just need to return the total.