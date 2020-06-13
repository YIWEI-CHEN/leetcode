import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._hash = {}
        self._array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._hash:
            return False
        self._hash[val] = len(self._array)
        self._array.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self._hash:
            idx = self._hash[val]
            last_element = self._array[-1]
            self._array[idx] = last_element
            self._hash[last_element] = idx
            self._array.pop()
            del self._hash[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self._array)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
