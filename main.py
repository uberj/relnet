import attr
from station import Station 
from spacetime import SpaceTime
from edge import Edge

def world_loop(spacetime):
    for station in spacetime.all_stations():
        waves = []
        station.observe()
        station.orient()
        station.decide()
        signals = station.act(spacetime)
        waves.extend(signals)


if __name__ == "__main__":
    i = Station(
            time = 0, name="i",
            is_tx_station=True,
            rx=False
    )
    j = Station(time = 0, name="j", is_tx_station=True, rx=False)
    d = Station(
            time = 0,
            name="d",
            is_tx_station=True,
            tx_action=lambda _: True,
    )
    c = Station(time = 0, name="c")


    st = SpaceTime([
        Edge(s1=i, s2=j, time_between=1),
        Edge(s1=i, s2=d, time_between=2),
        Edge(s1=i, s2=c, time_between=5),

        Edge(s1=j, s2=d, time_between=1),
        Edge(s1=j, s2=c, time_between=2),

        Edge(s1=c, s2=d, time_between=1)
    ])

    st.draw_graph()
