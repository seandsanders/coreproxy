coreproxy
=========

A proxy for making requests to Brave Core API

##1. Purpose
This project is intended to be a thin wrapper around calls to the Brave Core Service API Bindings for non-Python projects

see: https://github.com/bravecollective/api

##2. Features
Currently this project is under development and probably only suitable for other in-development projects.
The project creates a server which will listen for HTTP requests. It translates those requests into requests using
the core API Bindings and returns the result in JSON format.

It appears the API bindings use POST requests exclusively, so I've mirrored this in this application.

##3. Installation
Create a python virtual environment

    virutalenv coreproxy

Activate virutal environment

    cd coreproxy
    source bin/activate

Setup Brave Core Service API Bindings repository

    git clone https://github.com/bravecollective/api.git
    (cd api; python setup.py develop)

Setup Core Proxy repository

    git clone https://github.com/seandsanders/coreproxy
    (cd coreproxy; python setup.py develop)

Copy sample config and update it

    (cd coreproxy/brave/coreproxy; cp config.sample.py config.py; editor config.py)

Since the server is only supporting HTTP connections at the moment, you should never bind it to anything but localhost.
It requires your private ECDSA key to function and this should not be transmitted over the network insecurely.

##4. Usage
Currently the server needs to be started manually. I plan on adding stuff to have it run as a service here soon.

    # Be sure the virtual environment is activated
    (cd coreproxy/brave/coreproxy; python coreproxy.py)

Make an HTTP POST request to the host and port in your config.py. The POST data should include whatever is required
for the particular call you're making. The path should be the path API would expect.

In addition, the POST request should include 4 additional parameters (the same ones normally found in the API config)

    coreproxy_endpoint: full path to core server (https://core.braveineve.com/api)
    coreproxy_identity: application ID for application registered in core
    coreproxy_private: hexlified private key string
    coreproxy_public: hexlified public key string

Example w/ curl

    curl --data "coreproxy_endpoint=https://core.braveineve.com/api&coreproxy_identity={ID}&coreproxy_private={private_key}&coreproxy_public={public_key}&success=http://example.net/success&failure=http://example.net/nolove" http://127.0.0.1:8080/core/authorize/

##5. License

Brave Core Proxy has been released under the MIT Open Source license.

###5.1 The MIT License

Copyright (C) 2014 Sean Sanders and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.