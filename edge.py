import attr
from pprint import pprint

@attr.s
class Edge(object):
    s1 = attr.ib()
    s2 = attr.ib()
    time_between = attr.ib(factory=int)

    def recieve(self, m):
        rx.append((self.time, rx))

    def tick(self):
        self.time += 1
        print("station: " + self.name)
        print("rx stack: ")
        pprint(self.rx)
