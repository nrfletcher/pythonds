# Sequential search is O(n), binary search is O(logn), can we do better? We can with hashing


# A function for generating a hash value for a string
def string_hash(string, tsize):
    sum = 0
    for i in string:
        sum += ord(i)

    return sum % tsize


# To avoid anagram collisions utilize a weighting system
def string_hash_weighted(string, tsize):
    sum = 0
    weight = 1
    for i in string:
        sum += ord(i) + weight
        weight += 1

    return sum % tsize


# The map data structure
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.data))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = None
        found = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


table = HashTable()
table[54] = "BMW"
table[22] = "Mercedes"
table[99] = "Audi"
table[45] = "Jaguar"
print(table.slots)
