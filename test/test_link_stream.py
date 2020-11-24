import pytest
import networkx as nx
from LinkStream.LinkStream import LinkStream
from LinkStream.LinkStreamError.InvalidLinkStreamError import InvalidLinkStreamError


def test_add_vertex():
    link_stream = LinkStream()
    link_stream.add_vertex(1)
    assert link_stream.get_vertexes() == set([1])


def test_single_edge():
    link_stream = LinkStream()
    link_stream.add_vertex(1)

    g = nx.Graph()
    g.add_nodes([1, 2])
    g.add_edge(1, 2)
    link_stream.add_graph(g)


def test_add_illegal_graph_not_subset():
    link_stream = LinkStream()
    link_stream.add_vertexes([1, 2])

    g = nx.Graph()
    g.add_nodes([1, 2, 3])
    with pytest.raises(InvalidLinkStreamError, match=r"f'These nodes will be missing at time {0}: (1,2,3)'"):
        link_stream.add_graph(g)