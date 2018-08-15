import attr
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

@attr.s
class SpaceTime(object):
    edges = attr.ib(factory=list)

    def can_receive(self, station1, station2):
        return True

    def time_between(self, station1, station2):
        for e in self.edges:
            if e.s1 is station1 and e.s2 is station2:
                return e.time_between
            if e.s2 is station1 and e.s1 is station2:
                return e.time_between
        return -1

    def all_stations(self):
        stations = set()
        for e in self.edges:
            stations.add(e.s1)
            stations.add(e.s2)
        return stations

    def draw_graph(self):
        G=nx.Graph()
        for e in self.edges:
            G.add_node(e.s1)
            G.add_node(e.s2)
            G.add_edge(
                    e.s1,
                    e.s2,
                    weight=e.time_between,
                    object={'time_between': e.time_between})
        pos=nx.spring_layout(G)
        edge_labels = {
                (edge[0], edge[1]):
                edge[2]['object'] for edge in
                G.edges(data=True)
        }

        edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(
                G,pos,
                edge_labels=edge_labels)
        nx.draw(G, with_labels=True)
        plt.show()
