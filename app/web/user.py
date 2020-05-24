from . import web


@web.route('/hello1')
def hello1():
    return "hello1"
