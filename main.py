import argparse

import boolean

from BooleanEntities.Formula import Formula
from match_building.match_building import build_link_stream_from_formula, build_matching


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

    # Wrap formula and clauses both in boolean and string format
    # for easy manipulation

    args = parser.parse_args()
    text_formula = args.formula
    algebra = boolean.BooleanAlgebra()
    formula = Formula(algebra, text_formula)

    # Build link stream for given gamma e given formula
    gamma = args.gamma
    formula_link_stream = build_link_stream_from_formula(
        algebra, formula, gamma
    )

    # Hardcoded by now
    assignment = {
        boolean.Symbol('w'): algebra.TRUE,
        boolean.Symbol('x'): algebra.FALSE,
        boolean.Symbol('y'): algebra.TRUE,
        boolean.Symbol('z'): algebra.FALSE
    }
    matching = build_matching(algebra, formula, assignment, formula_link_stream, gamma)
    print(formula_link_stream)
    print('-------------')
    print('-------------')
    print('-------------')
    print(matching)
