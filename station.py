import attr
from typing import List, Mapping
from t import Message, RXClaim


@attr.s(hash=False)
class StationLogEntry(object):
        log_entry_time = attr.ib(type=int)
        sending_station_name_claim = attr.ib(type=str)
        sending_station_time_claim = attr.ib(type=int)
        name_of_who_the_sender_says_they_heard = attr.ib(type=str)
        time_claim_who_the_sender_says_they_heard = attr.ib(type=int)
        has_broadcast = attr.ib(type=bool, default=False)


@attr.s(hash=False)
class Station(object):
    name = attr.ib()
    tx_action = attr.ib(default='')
    rx = attr.ib(default=[], type=List[dict])
    is_tx_station = attr.ib(default=False)
    time = attr.ib(default=0)
    rx_claims = List[RXClaim]
    rx_claim_log = attr.ib(default=Mapping[str, List[StationLogEntry]])

    def observe(self, messages: List[Message]):
        # Listen to messages and store them well so we can make decisions about
        # them
        for message in messages:
            message.sending_station_name
            for rx_claim in message.rx_claims:
                self.record_log(message, rx_claim)

    def record_log(self, message, rx_claim):
        station_log = self.rx_claim_log.setdefault(
                message.sending_station_name, [])

        station_log.append(
                StationLogEntry(
                    self.time,
                    message.sending_station_name,
                    message.time_sent,
                    rx_claim.station_claim_name,
                    rx_claim.station_time_claim
                ))

    def orient(self, orient):
        []

    def decide(self, orient):
        pass

    def act(self, orient) -> Message:
        # Need to send the time I heard from a station and what time I heard
        # someone else got from the station
        claims_to_broadcast = []
        for station_name: str, log_entries in self.rx_claim_log.items():
            for log_entry in log_entries:
                if not log_entry.has_broadcast:
                    claims_to_broadcast.append(RXClaim(
                        station_name,
                        log_entry.sending_station_time_claim
                    ))

        return Message(self.name, self.time, to_broadcast)

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
