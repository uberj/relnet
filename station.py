import attr
from pprint import pprint
import pdb

@attr.s(hash=False)
class Station(object):
    name = attr.ib()
    tx_action = attr.ib(default='')
    rx = attr.ib(default=[])
    is_tx_station = attr.ib(default=False)
    time = attr.ib(default=0)


    def observe(self, messages):
        # Listen to messages and store them well so we can make decisions about
        # them
        messages
        pass

    def orient(self, orient):
        []

    def decide(self, orient):
        {}

    def act(self, orient):
        []

    def advance_time(self, amount):
        self.time += amount

    def should_tx():
        return True

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name
