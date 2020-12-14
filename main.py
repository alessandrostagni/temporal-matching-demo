import argparse

import boolean
import networkx as nx

from LinkStream import LinkStream

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
    text_formula = args.formula

    m = text_formula.count('(')
    gamma = args.gamma

    formula = algebra.parse(text_formula)
    print(formula.symbols)

    link_stream = LinkStream.LinkStream()

    for s in formula.symbols:
        for t in range(0, (m+1) * (gamma -1)):
            g = nx.Graph()
            g.add_edge(f'{s}=', f'{s}+')
            g.add_edge(f'{s}=', f'{s}-')
            link_stream.add_graph(g)