from station import Station 
from spacetime import SpaceTime
from edge import Edge

if __name__ == "__main__":
    i = Station(time = 0, name="i")
    j = Station(time = 0, name="j")
    d = Station(time = 0, name="d")
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
