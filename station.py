import attr
from pprint import pprint
import pdb

@attr.s(hash=False)
class Station(object):
    rx = attr.ib(factory=list)
    time = attr.ib(default=0)
    name = attr.ib(factory=str)

    def recieve(self, m):
        rx.append((self.time, rx))

    def tick(self):
        self.time += 1
        print("station: " + self.name)
        print("rx stack: ")
        pprint(self.rx)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name
