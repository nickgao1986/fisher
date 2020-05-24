from flask import Flask, make_response, jsonify, Blueprint, request

from yushu_book import YuShuBook
from . import web


@web.route('/hello')
def hello():
    q = request.args['q']
    page = request.args['page']
    print("<<<q="+q+"page="+page)
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    q = '9787501524044'
    result = YuShuBook.search_by_isbn(q)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
    return jsonify(result)
