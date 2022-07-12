"""Singleton class"""

import random

class Owner:
    _id : int = 0
    def get(self):
        if (self._id != 0): return self._id
        self._id = random.randint(1,10)
        return self._id
owner = Owner()

print(owner.get())
print(owner.get())
print(owner.get())
