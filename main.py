# -*- coding:utf-8 -*-
# Author: Jason Lee

from wsgiref.simple_server import make_server

from backend.settings import headers
from backend.urls import urlpatterns


def get_handler(path):
    handler = urlpatterns.get(path, None)
    if handler:
        return handler
    else:
        return None

def application(environ, start_response):
    func = get_handler(environ['PATH_INFO'])
    if func:
        result = func(environ)
        reason = '200 OK'
    else:
        result = '<h1>404 Not found...</h1>'.encode()
        reason = '404 Not Found'

    start_response(reason, headers)
    return [result]

httpd = make_server('', 8000, application)
httpd.serve_forever()