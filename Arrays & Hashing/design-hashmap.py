class LinkedNode:
    def __init__(self, key= -1, value= -1, next=None):
        self.key = key 
        self.value = value 
        self.next = next 

class MyHashMap:

    def __init__(self):
        size = 1000
        self.mapping = [LinkedNode() for i in range(size)]

    def put(self, key: int, value: int) -> None: 
        current = self.mapping[key % 1000]
        while current.next: 
            if current.next.key == key:
                current.next.value = value  
                return
            current = current.next
        current.next = LinkedNode(key,value)

    def get(self, key: int) -> int:
        current = self.mapping[key % 1000]
        while current and current.next: 
            if current.next.key == key: 
                return current.next.value
            current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        current = self.mapping[key % 1000]
        while current and current.next: 
            if current.next.key == key: 
                current.next = current.next.next
            current = current.next
        


# For this problem we needed to make a hashmap without using any built in hash table. To do this I used a list of 
# linked lists which stores the mappings as a linked list node. Once again like design hashset, we use a simple hash 
# of modding the key before inserting and we just create a new linkednode to insert into the linked list. One issue 
# that occured was in the remove method, which required to check both the current node and the next node. This was because 
# if we just had the next node, once we remove it and move on to the new node, this new node might be the end and has no 
# .next element to it. This would end up in an error, so we check to see if we are the second to last node instead and that
# works out great.