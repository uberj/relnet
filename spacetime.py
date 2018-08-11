import attr
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

@attr.s
class SpaceTime(object):
    edges = attr.ib(factory=list)

    def draw_graph(self):
        G=nx.Graph()
        for e in self.edges:
            G.add_node(e.s1)
            G.add_node(e.s2)
            G.add_edge(e.s1, e.s2, weight=e.time_between, object={'time_between': e.time_between})
        labels = nx.get_edge_attributes(G,'time_between')
        nx.draw(G, with_labels=True, edge_lables=labels)
        plt.show()
