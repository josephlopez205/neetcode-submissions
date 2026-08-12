class MyHashMap:

    def __init__(self):
        self.hashmap = []
        self.keys = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.hashmap.append([key, value])
        else:
            index = self.keys.index(key)
            self.hashmap[index][1] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            index = self.keys.index(key)
            return self.hashmap[index][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.hashmap.pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)