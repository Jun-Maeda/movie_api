#!/usr/local/bin/python3
import cgitb
cgitb.enable()

from wsgiref.handlers import CGIHandler
from html_set import app
CGIHandler().run(app)


# from sys import path
#
# path.insert(0, '/python/')
# from html_set import app
# class ProxyFix(object):
#   def __init__(self, app):
#       self.app = app
#   def __call__(self, environ, start_response):
#       # ※要書き換え
#       environ['SERVER_NAME'] = "s1001.coreserver.jp"
#       environ['SERVER_PORT'] = "21"
#       environ['REQUEST_METHOD'] = "GET"
#       environ['SCRIPT_NAME'] = ""
#       environ['PATH_INFO'] = "/"
#       environ['QUERY_STRING'] = ""
#       environ['SERVER_PROTOCOL'] = "HTTP/1.1"
#       return self.app(environ, start_response)
# if __name__ == '__main__':
#    app.wsgi_app = ProxyFix(app.wsgi_app)
#    CGIHandler().run(app)
