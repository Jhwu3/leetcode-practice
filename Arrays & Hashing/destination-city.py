class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hasDestination = set()
        allLocation = set()
        for flight in paths: 
                hasDestination.add(flight[0])
                allLocation.add(flight[0])
                allLocation.add(flight[1])

        return (allLocation - hasDestination).pop()
        
        
# For this problem it gives us an array of paths, basically just pairs of locations, as elements in a list: 
# For example:  paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] and what we need to do is 
# find the location that is destination city. and this just means that none of the paths leads out from that city.
# And so my idea was to have two sets, one with all the locations and one for all the locations that show up as the 
# first destination of a path. since the question guarantees that the paths do not form a cycle, we can just find the
# difference between the two sets and return that result.