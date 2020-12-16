import logging
import os

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic

from LinkStream.LinkStreamError import InvalidLinkStreamError


class LinkStream:
    def __init__(self, path=None):
        self.vertexes = set()
        self.graphs = []
        self.logger = logging.getLogger('LINK_STREAM_LOGGER')
        if path is not None:
            self._load_from_filename(path)

    def _load_from_filename(self, path):
        old_t = None
        g = None
        with open(path) as f:
            for line in f:
                record = [int(r) for r in line.strip().split()]
                new_t = record[2]
                if old_t != new_t:
                    if g is not None:
                        self.add_graph(g)
                    # Fill eventual gaps if new_t > old_t + 1
                    if old_t is not None:
                        if new_t > old_t + 1:
                            while len(self.graphs) != new_t:
                                g = nx.Graph()
                                g.add_nodes_from(self.vertexes)
                                self.graphs.append(g)
                        elif new_t < old_t:
                            raise InvalidLinkStreamError(
                                't dimension needs to be incremental!'
                            )
                    g = nx.Graph()
                    old_t = new_t
                if record[0] != -1 and record[1] != -1:
                    self.vertexes.update((record[0], record[1]))
                    g.add_nodes_from((record[0], record[1]))
                    g.add_edge(record[0], record[1])
            self.graphs.append(g)

    def write_to_file(self, path):
        with open(path, 'w') as w:
            for t, g in enumerate(self.graphs):
                for e in g.edges:
                    if e[0] < e[1]:
                        w.write(f'{e[0]} {e[1]} {t}\n')

    def save_to_file(self, path, cumulative):
        colors = [y for x, y in mcolors.CSS4_COLORS.items()]
        os.mkdir(path)
        prefix = os.path.split(path)[-1]
        for t, g in enumerate(self.graphs):
            nx.draw(
                g, with_labels=True, node_color=colors[t],
                pos=nx.spring_layout(g)
            )
            plt.savefig(os.path.join(path, f'{prefix}_{t}.png'))
            if not cumulative:
                plt.clf()
        plt.clf()

    def __str__(self):
        if len(self.graphs) == 0:
            return 'Link stream is empty!'
        out = 'Nodes: '
        for n in self.vertexes:
            out += f'{n}, '
        out = out[:-2] + '\n'
        out += '------\n'
        for t in range(len(self.graphs)):
            g = self.graphs[t]
            out += f't: {t}\n'
            out += 'Edges: '
            out_edges = ""
            for e in g.edges():
                out_edges += f'{e}, '
            out += out_edges[:-2] + '\n'
            out += '------\n'
        return out

    def __eq__(self, link_stream):
        if len(self.graphs) != len(link_stream.graphs):
            return False
        for g1, g2 in zip(self.graphs, link_stream.graphs):
            if not is_isomorphic(g1, g2):
                return False
        return True

    def get_vertexes(self):
        return self.vertexes

    def add_vertex(self, v):
        self.vertexes.add(v)

    def add_vertexes(self, vertexes):
        self.vertexes.update(vertexes)

    def add_graph(self, g):
        t = len(self.graphs)
        nodes_set = set(g.nodes)
        if not nodes_set.issubset(self.vertexes):
            raise InvalidLinkStreamError(
                f'These nodes will be missing at time {t}: '
                f'{nodes_set.difference(self.vertexes)}'
            )
        if not nodes_set.issuperset(self.vertexes):
            raise InvalidLinkStreamError(
                f'These nodes should not be present at time {t}: '
                f'{self.vertexes.difference(nodes_set)}'
            )
        self.graphs.append(g)

    def get_graph(self, t):
        return self.graphs[t]

    def get_graphs(self):
        return self.graphs

    def get_gamma_link_stream(self, gamma):
        gamma_link_stream = LinkStream()

        # Initialise empty graphs for gamma link stream
        for _ in self.graphs:
            gamma_link_stream.add_graph(nx.Graph())

        gamma_link_stream.add_vertexes(self.get_vertexes())

        checked_edges = set()

        # For every graph
        for t1, g1 in enumerate(self.graphs):
            # For every edge in the graph
            for e in g1.edges:
                # Take edge into account
                if e not in checked_edges:
                    edge_presence = []
                    for g2 in self.graphs[t1 + 1:]:
                        if e in g2.edges:
                            edge_presence.append(1)
                        else:
                            edge_presence.append(0)
                    for t in range(len(edge_presence)):
                        if e in self.graphs[t1 + t].edges and \
                           1 in edge_presence[t:t + gamma]:
                            gamma_link_stream.graphs[t1 + t].add_edge(*e)
        return gamma_link_stream
