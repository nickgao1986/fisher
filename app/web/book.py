from flask import Flask, make_response, jsonify, Blueprint, request

from yushu_book import YuShuBook
from . import web


# from app.form.book import SearchForm
from ..form.book import SearchForm


@web.route('/hello')
def hello():
    form = SearchForm(request.args)
    print("isvalidate="+"aa" if form.validate() else "bb")
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        print("q="+q)
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    q = '9787501524044'
    result = YuShuBook.search_by_isbn(q)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
    return jsonify(result)
