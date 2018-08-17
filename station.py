import attr
from typing import List
from types import Message


@attr.s(hash=False)
class Station(object):
    name = attr.ib()
    tx_action = attr.ib(default='')
    rx = attr.ib(default=[], type=List[dict])
    is_tx_station = attr.ib(default=False)
    time = attr.ib(default=0)

    def observe(self, messages: List[Message]):
        # Listen to messages and store them well so we can make decisions about
        # them
        for message in messages:
            message.sending_station_name
            for rx_claim in rx_claims:
                station_name, time_claim = rx_claim
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

    def should_tx(self):
        return True

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name
