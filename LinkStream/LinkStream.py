import logging

import networkx as nx

from LinkStream.LinkStreamError import InvalidLinkStreamError

class LinkStream:
    def __init__(self):
        self.vertexes = set()
        self.graphs = []
        self.logger = logging.getLogger('LINK_STREAM_LOGGER')

    def __str__(self):
        if len(self.graphs) == 0:
            return 'Link stream is empty!'
        out = ''
        for t in range(self.graphs):
            out += f't: {t}\n'
            out += f'Nodes:'
            g = self.graphs[t]
            for n in g.nodes():
                out += f'{n}'
            out += f'Edges:'
            for e in g.edges():
                out += f'{e}'
        return out

    def get_vertexes(self):
        return self.vertexes

    def add_vertex(self, v):
        self.vertexes.add(v)

    def add_vertexes(self, vertexes):
        self.vertexes.update(vertexes)

    def add_graph(self, g):
        t = len(self.vertexes)
        nodes_set = set(g.nodes)
        if not nodes_set.issubset(self.vertexes):
            raise InvalidLinkStreamError(f'These nodes should not be present at time {t}: {nodes_set}')
        if not nodes_set.issuperset(self.vertexes):
            raise InvalidLinkStreamError(f'These nodes will be missing at time {t}: {nodes_set}')
        self.graphs.add(g)

    def get_graph(self, t):
        return self.graphs(t)

    def get_gamma_link_stream(self, gamma):
        edge_dict = {}
        gamma_link_stream = LinkStream()

        for t in range(self.graphs):
            new_edge_dict = {}
            gamma_graph = nx.Graph()
            g = self.graphs[t]
            for e in g.edges:
                if e not in edge_dict:
                    new_edge_dict[e] = 1
                else:
                    new_edge_dict[e] = edge_dict[e] + 1
                    if new_edge_dict[e] >= gamma:
                        gamma_graph.add_edge(e)
            edge_dict = new_edge_dict
            gamma_link_stream.add_graph(g)
        return gamma_link_stream






