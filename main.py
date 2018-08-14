import attr
from station import Station 
from spacetime import SpaceTime
from edge import Edge

def world_loop(spacetime, duration_clicks=20):
    # Inboxes are magic. They recieve a wave and delay the wave for delivary
    # until the distance the wave has traveled makes sense. An inbox
    # knows the source coordinate and the destination coordinate and will delay
    # delivery relative to the distance between the two coordinates.
    inboxes = make_inboxes(spacetime, spacetime.all_stations())
    for t in range(duration_clicks):
        waves = []
        for station in spacetime.all_stations():
            messages = inboxes.get(station.name).get_arrived_messages()

            # Inputs are recieved during observe
            station.observe(messages)

            # Past time clicks are accounted for during orient
            station.orient()

            # Hypothesis
            station.decide()

            # Test
            message = station.act(spacetime)

            # Later, the world may deliver these messages
            waves.append((station, message))

        # The world delivers a station's message to all other stations
        for station, message in waves:
            for other_station in spacetime.all_stations():
                if station is other_station:
                    continue

                if not spacetime.can_receive(station, other_station):
                    continue

                # We calculate the time delay for delivery. The inbox will
                # delay delivery for that many time clicks.
                tdelay = spacetime.time_between(station, other_station)
                inboxes.get(other_station.name).deliver((t, message))

        for inbox in inboxes:
            inblox.advance_time()

        for station in spacetime.all_stations():
            station.advance_time()

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
