import attr
from typing import List


@attr.s
class RXClaim:
    # The name of the station bring received
    station_name_claim = attr.ib(type=str)
    # The time the station claimed to have sent the message
    station_time_claim = attr.ib(type=int)


@attr.s
class Message:
    sending_station_name = attr.ib(type=str)
    time_sent = attr.ib(type=int)
    rx_claims = attr.ib(type=List[RXClaim])
