class arrayDictionary:

    #initializes with arrays for keys and values
    def __init__(self):
        self.keys = []
        self.values = []

    #appends new keys and values
    def put(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    #finds index of a given key, N
    def findIndex(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return i
        return None

    #using find index method, removes indexes at both lists
    def remove(self, key):
        index = self.findIndex(key)
        if index!= None:
            del self.keys[index]
            return self.values.pop(index)
        return None

    #checks if the key is in self.keys
    def contains(self, key):
        return key in self.keys

    #checks length of keys to see if it's empty
    def isEmpty(self):
        return len(self.keys)==0

    #returns length of keys
    def size(self):
        return len(self.keys)

    #returns keys
    def get_keys(self):
        return self.keys

    #returns values
    def get_values(self):
        return self.values