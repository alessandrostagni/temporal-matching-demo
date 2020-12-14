import argparse
import re

import boolean
import networkx as nx

from LinkStream import LinkStream


#def appears_in_clauses(formula)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        metavar='gamma', type=int,
        dest='gamma', help='Gamma parameter for gamma link stream'
    )
    parser.add_argument(
        metavar='formula',
        dest='formula', help='A formula in CNF'
    )
    args = parser.parse_args()
    algebra = boolean.BooleanAlgebra()
    
    # Keep formula and clauses both in boolean and string format
    # for easy manipulation
    
    text_formula = args.formula
    formula = algebra.parse(text_formula)
    text_clauses = re.findall(r'\([a-z~| ]+\)', text_formula)
    clauses = [algebra.parse(text_clause) for text_clause in text_clauses]

    m = text_formula.count('(')
    gamma = args.gamma

    link_stream = LinkStream.LinkStream()

    # Initialise link stream with nodes

    for s in formula.symbols:
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
    
    for s in formula.symbols:
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
                print(s)
                print(t)
                print(i)
                print(text_clauses)
                print('-----')
                if len(re.findall(f"[^~]{s}", text_clauses[i])) > 0:
                    print('MEOW')
                    g.add_edge('c', f'{s}{i}++')
                if len(re.findall(f"~{s}", text_clauses[i])) > 0:
                    g.add_edge('c', f'{s}{i}--')
    print(link_stream)
    