import re

import networkx as nx

from LinkStream import LinkStream
from BooleanEntities.Clause import Clause


def get_clauses(algebra, formula):
    text_clauses = re.findall(r'\([a-z~| ]+\)', formula.get_text_formula()) 
    clauses = [Clause(algebra, text_clause) for text_clause in text_clauses]
    return clauses


def build_link_stream_from_clause(algebra, formula, gamma):

    clauses = get_clauses(algebra, formula)
    m = len(clauses)
    link_stream = LinkStream.LinkStream()

    # Initialise link stream with nodes

    boolean_formula = formula.get_boolean_formula()

    for s in boolean_formula.symbols:
        link_stream.add_vertexes([
            f'{s}=', f'{s}+', f'{s}-',
        ])
        for i in range(0, m):
            link_stream.add_vertexes([
                f'{s}{i}++', f'{s}{i}--',
            ])

    # Add graphs with nodes for the whole interval
    for t in range(0, (m+1) * gamma):
        g = nx.Graph()
        g.add_nodes_from(link_stream.vertexes)
        link_stream.add_graph(g)

    for s in boolean_formula.symbols:
        # Initialise Evar
        for t in range(0, (m+1) * gamma):
            g = link_stream.get_graph(t)
            g.add_edge(f'{s}=', f'{s}+')
            g.add_edge(f'{s}=', f'{s}-')
        for i in range(0, m):
            for t in range(i * gamma + 1, (i+1) * gamma + 1):
                g = link_stream.get_graph(t)
                link_stream.add_vertexes(
                    [f'{s}{i}++', f'{s}{i}--', 'c']
                )
                g.add_edge(f'{s}+', f'{s}{i}++')
                g.add_edge(f'{s}-', f'{s}{i}--')

                # Initialise Ecla
                if len(re.findall(f"[^~]{s}", clauses[i].get_text_clause())) > 0:
                    g.add_edge('c', f'{s}{i}++')
                if len(re.findall(f"~{s}", clauses[i].get_text_clause())) > 0:
                    g.add_edge('c', f'{s}{i}--')
    return link_stream


def build_match(algebra, formula, assignment, link_stream):
    clauses = get_clauses(algebra, formula)
    m = len(clauses)
    link_stream = LinkStream()
