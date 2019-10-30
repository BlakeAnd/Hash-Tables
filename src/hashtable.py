# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            new_list = LinkedList()
            new_list.add_to_head({key: value})
            self.storage[index] = new_list 
        else:
            current_list = self.storage[index]
            current_list.add_to_head({key: value})            
        # print(f"insertion: {self.storage}")



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] != None and self.storage[index].head != None:
            print("OK")
            self.storage[index].remove(key)
        else:
            print("this key empty, yeet")
            return None
        # print(f"removal: {self.storage}")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # print(f"retreival: {index} is {self.storage}")
        if self.storage[index] is None or self.storage[index].head is None:
            return None
        else:
            return self.storage[index].contains(key)
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        array = []
        for i in range(0, self.capacity):
            print("curr index", self.storage[i])
            while self.storage[i] != None and self.storage[i].head != None:
                head = self.storage[i].pop_head()
                print("head", head.value)
                array.append(head.value)
        # print("arr", array)
        self.capacity *= 2
        self.storage = [None] * self.capacity  
        for i in range(0, len(array)):
            # key = array[i].keys()
            # print("arr", key)
            # self.insert array[i]
            for key in array[i]:
                # print("ok", key)
                # print("ok", array[i].get(key))
                value = array[i].get(key)
                self.insert(key, value)
        print("resize", self.storage)

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
        
class LinkedList:
    def __init__(self, set_head=None):
        self.head = set_head

    def add_to_head(self, value):
        # Create a head node
        new_node = Node(value, self.head)
        # Set current head to new node
        self.head = new_node

    def pop_head(self):
        head = self.head
        self.head = self.head.next
        return head

    def remove(self, value):
        '''
        Find and remove the node with the given value
        '''
        # print("OK")
        # print("remove", value)
        # print("remove", self.head)
        # print("remove", self.head.value.get(value))
        # If we have no head
        if not self.head:
            # print an error and return
            print("Error: Value not found")
        # If the head has our value
        elif self.head.value.get(value):
            # Remove the head by pointing self.head to head.next
            self.head = self.head.next
        # Else
        else:
            # Keep track of the parent node
            parent = self.head
            current = self.head.next
            # Walk through the linked list until we find a matching value
            while current:
                # If we find a matching value
                if self.head.value.get(value):
                    # Delete the node by pointing parent.next to node.next
                    parent.next = current.next
                    return
                current = current.next
            # If we get to the end and have not found the value, print error
            print("Error: Value not found")

    def contains(self, value):
        '''
        Return true if our LL contains the value
        '''
		# Fill this in
        current = self.head
        # print("curr", current.value.get(value))
        # print("val", value)
        
        while current:
            if current.value.get(value):
            	return current.value.get(value)
            current = current.next   
        return False  

if __name__ == "__main__":
    ht = HashTable(3)
 

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print(ht.remove("line_3"))

    # ht.resize()

    print("")
