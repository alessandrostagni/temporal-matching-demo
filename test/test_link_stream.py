import copy

import pytest
import networkx as nx
from networkx.algorithms.isomorphism import is_isomorphic

from LinkStream.LinkStream import LinkStream
from LinkStream.LinkStreamError import InvalidLinkStreamError


def test_create_link_stream_from_file():
    link_stream = LinkStream('test/test_cases/link_stream_1.txt')
    assert str(link_stream) == (
        'Nodes: 0, 1, 2, 3\n------\nt: 0\nEdges: '
        '(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)\n------\n'
        't: 1\nEdges: (0, 1), (0, 3), (1, 2), (1, 3), (3, 2)\n------\nt: 2\n'
        'Edges: (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)\n------\n'
    )


def test_create_link_stream_from_file_with_gaps():
    link_stream = LinkStream('test/test_cases/link_stream_gaps_1.txt')
    assert str(link_stream) == (
        'Nodes: 0, 1, 2, 3\n------\nt: 0\nEdges: '
        '(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)\n------\n'
        't: 1\nEdges: (0, 1), (0, 3), (1, 2), (1, 3), (3, 2)'
        '\n------\nt: 2\nEdges: \n------\nt: 3\nEdges: \n------\n'
        't: 4\nEdges: \n------\nt: 5\n'
        'Edges: (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)\n------\n'
    )


def test_equality_positive():
    link_stream = LinkStream('test/test_cases/link_stream_1.txt')
    link_stream_2 = LinkStream('test/test_cases/link_stream_1.txt')
    assert link_stream == link_stream_2


def test_equality_negative_length():
    link_stream = LinkStream('test/test_cases/link_stream_1.txt')
    link_stream_2 = LinkStream(
        'test/test_cases/expected_gamma_link_stream_1.txt')
    assert not link_stream == link_stream_2


def test_equality_negative_isomorphism():
    link_stream = LinkStream('test/test_cases/link_stream_1.txt')
    link_stream_2 = LinkStream('test/test_cases/link_stream_2.txt')
    assert not link_stream == link_stream_2


def test_write_link_stream_to_file(link_stream):
    g1 = nx.Graph()
    g1.add_nodes_from((1, 2, 3))
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)

    g2 = nx.Graph()
    g2.add_nodes_from((1, 2, 3))
    g2.add_edge(1, 3)

    g3 = nx.Graph()
    g3.add_nodes_from((1, 2, 3))
    g3.add_edge(2, 3)

    link_stream.add_vertexes((1, 2, 3))
    link_stream.add_graph(g1)
    link_stream.add_graph(g2)
    link_stream.add_graph(g3)

    link_stream.write_to_file(
        'test/test_output/test_write_link_stream_to_file.txt')
    assert open(
        'test/test_output/test_write_link_stream_to_file.txt'
    ).read() == \
        '1 2 0\n2 3 0\n1 3 1\n2 3 2\n'


def test_add_vertex(link_stream):
    link_stream.add_vertex(1)
    assert link_stream.get_vertexes() == set([1])


def test_add_vertexes(link_stream):
    link_stream.add_vertexes([1, 2, 3])
    assert link_stream.get_vertexes() == set([1, 2, 3])


def test_get_graph(link_stream):
    g1 = nx.Graph()
    g1.add_nodes_from((1, 2, 3))
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)

    g2 = nx.Graph()
    g2.add_nodes_from((1, 2, 3))
    g2.add_edge(1, 3)

    g3 = nx.Graph()
    g3.add_nodes_from((1, 2, 3))
    g3.add_edge(2, 3)

    link_stream.add_vertexes((1, 2, 3))
    link_stream.add_graph(g1)
    link_stream.add_graph(g2)
    link_stream.add_graph(g3)

    assert is_isomorphic(g2, link_stream.get_graph(1))


def test_get_graphs(link_stream):
    g1 = nx.Graph()
    g1.add_nodes_from((1, 2, 3))
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)

    g2 = nx.Graph()
    g2.add_nodes_from((1, 2, 3))
    g2.add_edge(1, 3)

    g3 = nx.Graph()
    g3.add_nodes_from((1, 2, 3))
    g3.add_edge(2, 3)

    link_stream.add_vertexes((1, 2, 3))
    link_stream.add_graph(g1)
    link_stream.add_graph(g2)
    link_stream.add_graph(g3)

    for t, g in enumerate(link_stream.get_graphs()):
        assert is_isomorphic(g, link_stream.graphs[t])


def test_add_illegal_graph_not_subset(link_stream):
    link_stream.add_vertexes([1, 2])

    g = nx.Graph()
    g.add_nodes_from([1, 2, 3, 4])
    with pytest.raises(
        InvalidLinkStreamError,
        match='These nodes will be missing at time 0: {3, 4}'
    ):
        link_stream.add_graph(g)


def test_add_illegal_graph_not_superset(link_stream):
    link_stream.add_vertexes([1, 2, 3, 4, 5])

    g = nx.Graph()
    g.add_nodes_from([1, 2, 3])
    with pytest.raises(
        InvalidLinkStreamError,
        match='These nodes should not be present at time 0: {4, 5}'
    ):
        link_stream.add_graph(g)


def test_str_empty_link_stream(link_stream):
    assert str(link_stream) == 'Link stream is empty!'


def test_eq_true(link_stream):
    g1 = nx.Graph()
    g1.add_nodes_from((1, 2, 3))
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)

    g2 = nx.Graph()
    g2.add_nodes_from((1, 2, 3))
    g2.add_edge(1, 3)

    g3 = nx.Graph()
    g3.add_nodes_from((1, 2, 3))
    g3.add_edge(2, 3)

    link_stream.add_vertexes((1, 2, 3))
    link_stream.add_graph(g1)
    link_stream.add_graph(g2)
    link_stream.add_graph(g3)

    link_stream_2 = copy.deepcopy(link_stream)
    assert link_stream.__eq__(link_stream_2)


def test_eq_false_by_edge(link_stream):
    g1 = nx.Graph()
    g1.add_nodes_from((1, 2, 3))
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)

    g2 = nx.Graph()
    g2.add_nodes_from((1, 2, 3))
    g2.add_edge(1, 3)

    g3 = nx.Graph()
    g3.add_nodes_from((1, 2, 3))
    g3.add_edge(2, 3)

    link_stream.add_vertexes((1, 2, 3))
    link_stream.add_graph(g1)
    link_stream.add_graph(g2)
    link_stream.add_graph(g3)
    link_stream_2 = copy.deepcopy(link_stream)
    link_stream_2.get_graph(1).add_edge(1, 2)

    assert not link_stream.__eq__(link_stream_2)


def test_eq_false_by_n_graphs(link_stream):
    g1 = nx.Graph()
    g1.add_nodes_from((1, 2, 3))
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)

    g2 = nx.Graph()
    g2.add_nodes_from((1, 2, 3))
    g2.add_edge(1, 3)

    g3 = nx.Graph()
    g3.add_nodes_from((1, 2, 3))
    g3.add_edge(2, 3)

    link_stream.add_vertexes((1, 2, 3))
    link_stream.add_graph(g1)
    link_stream.add_graph(g2)
    link_stream.add_graph(g3)
    link_stream_2 = copy.deepcopy(link_stream)

    g4 = nx.Graph()
    g4.add_nodes_from((1, 2, 3))
    g4.add_edge(1, 2)

    link_stream_2.add_graph(g4)

    assert not link_stream.__eq__(link_stream_2)


def test_str(link_stream):
    g1 = nx.Graph()
    g1.add_nodes_from((1, 2, 3))
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)

    g2 = nx.Graph()
    g2.add_nodes_from((1, 2, 3))
    g2.add_edge(1, 3)

    g3 = nx.Graph()
    g3.add_nodes_from((1, 2, 3))
    g3.add_edge(2, 3)

    link_stream.add_vertexes((1, 2, 3))
    link_stream.add_graph(g1)
    link_stream.add_graph(g2)
    link_stream.add_graph(g3)

    assert str(link_stream) == (
        'Nodes: 1, 2, 3\n------\nt: 0\nEdges: (1, 2), (2, 3)\n------\n'
        't: 1\nEdges: (1, 3)\n------\nt: 2\nEdges: (2, 3)\n------\n'
    )


def test_gamma_link_stream():
    link_stream = LinkStream('test/test_cases/link_stream_1.txt')
    expected_gamma_link_stream = LinkStream(
        'test/test_cases/expected_gamma_link_stream_1.txt')
    gamma_link_stream = link_stream.get_gamma_link_stream(2)
    assert str(gamma_link_stream) == str(expected_gamma_link_stream)


def test_to_d3():
    link_stream = LinkStream('test/test_cases/link_stream_1.txt')
    expected_dict = {
        0: {
            'directed': False, 'multigraph': False,
            'graph': {}, 'nodes': [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}],
            'links': [
                {'source': 0, 'target': 1}, {'source': 0, 'target': 2},
                {'source': 0, 'target': 3}, {'source': 1, 'target': 2},
                {'source': 1, 'target': 3}, {'source': 2, 'target': 3}
            ]
        },
        1: {
            'directed': False, 'multigraph': False,
            'graph': {}, 'nodes': [{'id': 0}, {'id': 1}, {'id': 3}, {'id': 2}],
            'links': [
                {'source': 0, 'target': 1}, {'source': 0, 'target': 3},
                {'source': 1, 'target': 2}, {'source': 1, 'target': 3},
                {'source': 3, 'target': 2}
            ]
        },
        2: {
            'directed': False, 'multigraph': False,
            'graph': {}, 'nodes': [{'id': 0}, {'id': 1}, {'id': 2}, {'id': 3}],
            'links': [
                {'source': 0, 'target': 1}, {'source': 0, 'target': 2},
                {'source': 0, 'target': 3}, {'source': 1, 'target': 3},
                {'source': 2, 'target': 3}
            ],
        },
    }
    assert link_stream.to_d3() == expected_dict
