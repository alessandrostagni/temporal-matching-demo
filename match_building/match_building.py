import random
import re

import networkx as nx

from LinkStream import LinkStream
from BooleanEntities.Clause import Clause

random.seed(3)


def get_clauses(algebra, formula):
    text_clauses = re.findall(r'\([a-z~| ]+\)', formula.get_text_formula()) 
    clauses = [Clause(algebra, text_clause) for text_clause in text_clauses]
    return clauses


def build_link_stream_from_formula(algebra, formula, gamma):

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
    link_stream.add_vertexes('c')

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


def chi(clauses):
    chi_nodes = []
    for i, c in enumerate(clauses):
        boolean_c = c.get_boolean_clause()
        text_c = c.get_text_clause()
        s = random.sample(boolean_c.symbols, 1)[0]
        if len(re.findall(f"[^~]{s}", c.get_text_clause())) > 0:
            chi_nodes.append(f'{s}{i}++')
        if len(re.findall(f"~{s}", c.get_text_clause())) > 0:
            chi_nodes.append(f'{s}{i}--')
    return chi_nodes


def build_matching(algebra, formula, assignment, link_stream, gamma):
    clauses = get_clauses(algebra, formula)
    chi_nodes = chi(clauses)
    m = len(clauses)
    matching = LinkStream.LinkStream()
    matching.add_vertexes(link_stream.get_vertexes())

    # Initialise matching with nodes from input link stream
    for i, g in enumerate(link_stream.get_graphs()):
        matching_g = nx.Graph()
        matching_g.add_nodes_from(g.nodes)
        matching.add_graph(matching_g)

    # Build matching from formula and assignment

    for i in range(m):
        g1 = matching.get_graph(i * gamma)
        g2 = matching.get_graph(i * gamma + 1)
        for s, val in assignment.items():
            if val == algebra.TRUE:
                g1.add_edge(f'{s}=', f'{s}+')
                if i > 0:
                    g2.add_edge(f'{s}=', f'{s}{i}--')
            else:
                g1.add_edge(f'{s}=', f'{s}-')
                if i>0:
                    g2.add_edge(f'{s}+', f'{s}{i}++')
        if i > 0:
            g2.add_edge(chi_nodes[i], 'c')
    return matching
