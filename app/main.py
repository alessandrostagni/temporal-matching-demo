import json
import os
import shutil

import boolean
from flask import Flask, request
from flask_cors import cross_origin

from BooleanEntities.Formula import Formula
from match_building.match_building import build_link_stream_from_formula, \
    build_matching

app = Flask(__name__)


@app.route('/get-graph', methods=['POST'])
@cross_origin()
def get_graph():
    try:
        data = request.get_json()

        text_formula = data['formula']
        algebra = boolean.BooleanAlgebra()
        formula = Formula(algebra, text_formula)

        # Build link stream for given gamma e given formula
        gamma = data['gamma']
        formula_link_stream = build_link_stream_from_formula(
            algebra, formula, gamma
        )

        assignment = {
            boolean.Symbol(x): (
                algebra.TRUE if data['assignment'][x] == 'True'
                else algebra.FALSE
            ) for x in data['assignment']
        }

        matching = build_matching(
            algebra, formula, assignment,
            formula_link_stream, gamma
        )
        if os.path.exists('.\\graphs\\link_stream'):
            shutil.rmtree('.\\graphs\\link_stream')
        if os.path.exists('.\\graphs\\matching'):
            shutil.rmtree('.\\graphs\\matching')
        res = {'linkStream': formula_link_stream.to_d3(),
               'matching': matching.to_d3()}
    except Exception:
        return 'Bad Request', 400
    return json.dumps(res)


@app.route('/heartbeat', methods=['GET'])
@cross_origin()
def heartbeat():
    return json.dumps({'ok': 1})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
