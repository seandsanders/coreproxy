from binascii import unhexlify
from ecdsa import SigningKey, VerifyingKey, NIST256p
from hashlib import sha256
from webob import Response, Request, exc
from brave.api.client import API
from brave.coreproxy.config import settings

REQUIRED_KEYS = {'coreproxy_endpoint', 'coreproxy_identity', 'coreproxy_private', 'coreproxy_public'}


def pop_auth_values(post_dict):
    endpoint = post_dict.pop('coreproxy_endpoint')
    identity = post_dict.pop('coreproxy_identity')
    private = SigningKey.from_string(unhexlify(post_dict.pop('coreproxy_private')), curve=NIST256p, hashfunc=sha256)
    public = VerifyingKey.from_string(unhexlify(post_dict.pop('coreproxy_public')), curve=NIST256p, hashfunc=sha256)
    return endpoint, identity, private, public


def application(environ, start_response):
    request = Request(environ)
    if request.method != 'POST':
        response = exc.HTTPMethodNotAllowed("Only POST allowed")
        return response(environ, start_response)

    post_dict = dict(request.POST)
    if not REQUIRED_KEYS.issubset(set(post_dict.keys())):
        response = exc.HTTPBadRequest('Request missing %s' % list(REQUIRED_KEYS - set(post_dict.keys())))
        return response(environ, start_response)

    endpoint, identity, private, public = pop_auth_values(post_dict)

    api = API(endpoint, identity, private, public)
    path_segments = request.path_info.strip('/').split('/')
    api_call = reduce(getattr, path_segments, api)
    json_response = api_call(**post_dict)

    if json_response is None:
        response = exc.HTTPBadRequest('Error processing request')
        return response(environ, start_response)

    response = Response(json=json_response)
    return response(environ, start_response)

if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(application, host=settings['server']['host'], port=settings['server']['port'])