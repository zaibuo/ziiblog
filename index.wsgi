#def application(environ, start_response):
#    start_response('200 ok', [('content-type', 'text/plain')])
#    return ['Hello, SAE!']


import sae
from mysite import wsgi

#def app(environ, start_response):
#    status = '200 OK'
#    response_headers = [('Content-type', 'text/plain')]
 #   start_response(status, response_headers)
 #   return ['Hello, world!']

application = sae.create_wsgi_app(wsgi.application)