class UndergroundSystem:

    def __init__(self):
        self.avg = {}
        self.system = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.system:
            self.system[id] = [stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        combo = self.system[id][0] +" "+ stationName
        if combo in self.avg: 
            self.avg[combo][0] += (t - self.system[id][1])
            self.avg[combo][1] += 1
        else: 
            self.avg[combo] = [t - self.system[id][1],1]
        del self.system[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[startStation + " " + endStation][0] / self.avg[startStation + " " + endStation][1]




# This problem asks to us to create an underground system that has three methods, checkIn, checkOut and getAverageTime. 
# So to create thses features i used two dictionaries, one for passengers who are still in the system, and another for 
# keeping track of average time between systems. The avg dictionary would have key value pairs where the keys are the 
# string combination of the two stations, and the value has a pair containg the total time elapses and total passengers checked out.
# Then all we need to do is every time a passenger checksOut, we can add the time difference into that specific train station 
# start and end combo and increment the total passengers. Then when we need to get the averageswe just divide the total time 
# elapsed by the total customers checked out. 