class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(size)]

    def add(self, key: int) -> None:
        index = self.myHash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self.myHash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.myHash(key)
        return key in self.buckets[index]

    def myHash(self, key: int) -> int:
        return key % self.size
        


this problem asks us to create a hashset without using any built in hash table libraries. so the way 
to do this is to create a list of list and using a simple hashing method, we can achieve a constant time 
add, remove and contains method. And to adress the collisions, we just append the colliding value into the 
correct list. 


