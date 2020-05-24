from flask import Flask, make_response, jsonify, Blueprint

web = Blueprint('web', __name__)

@web.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    q = '9787501524044'
    result = YuShuBook.search_by_isbn(q)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
    return jsonify(result)
