from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML

from flask import Flask, jsonify, request
from flask_cors import CORS

from app.schema import executable_schema

app = Flask(__name__)
CORS(app)

if app.debug:
  @app.route('/v2/graphql', methods=['GET'])
  def graphql_playground():
    # On GET request serve GraphQL Playground
    return PLAYGROUND_HTML, 200


@app.route('/v2/graphql', methods=['POST'])
def graphql_server():
    # GraphQL queries are always sent as POST
  data = request.get_json()
  # Note: Passing the request to the context is optional.
  # In Flask, the current request is always accessible as flask.request
  success, result = graphql_sync(
      executable_schema,
      data,
      context_value=request,
      debug=app.debug
  )
  status_code = 200 if success else 400
  return jsonify(result), status_code


if __name__ == '__main__':
  app.run()
