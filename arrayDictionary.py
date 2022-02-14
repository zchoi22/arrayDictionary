class arrayDictionary:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def findIndex(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return i
        return None

    def remove(self, key):
        index = self.findIndex(key)
        if index!= None:
            del self.keys[index]
            return self.values.pop(index)
        return None

    def contains(self, key):
        return key in self.keys

    def isEmpty(self):
        return len(self.keys)==0

    def size(self):
        return len(self.keys)

    def get_keys(self):
        return self.keys

    def get_values(self):
        return self.values