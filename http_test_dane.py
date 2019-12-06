#!/usr/bin/env python

"""
HTTP Test DANE.

This implements a DANE for testing purposes according to ISO/IEC 23009-5 SAND.
It implementes a HTTP SAND Channel that a DASH client can connect to.
SAND messages that may be sent and received by this test DANE do not reflect
real operations but merely serve as example behaviour.

Copyright (c) 2019-, TNO
All rights reserved.

See AUTHORS for a full list of authors.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the
names of its contributors may be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import logging

from flask import Flask
from flask import request
from flask import Response

from werkzeug.routing import Rule

import click

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

MESSAGES = {
    "DaneCapabilitiesPC": 
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<SANDMessage xmlns="urn:mpeg:dash:schema:sandmessage:2016" senderId="abc1234" generationTime="2016-02-21T11:20:52-08:00">'
          '<DaneCapabilities messageId="45678" messageSetUri="http://dashif.org/guidelines/sand/modes/pc"></DaneCapabilities>'
        '</SANDMessage>'
}

APP = Flask(__name__)
APP.debug = True
APP.url_map.add(Rule('/pc', endpoint='pc'))
APP.url_map.add(Rule('/metrics', endpoint='metrics'))

@APP.endpoint('pc')
def pc():
    """
    Receives first DSAH client request.
    """
    if request.method == "POST":
        logging.info("Received POST HTTP method")
        return Response(MESSAGES["DaneCapabilitiesPC"], 200, mimetype='application/sand+xml')
    else:
        logging.info("Received %s HTTP method", request.method)
        return ("", 200)

@APP.endpoint('metrics')
def pc():
    """
    Receives metrics from DASH client.
    """
    if request.method == "POST":
        logging.info("Received POST HTTP method")
        return ("OK", 200)
    else:
        logging.info("Received %s HTTP method", request.method)
        return ("", 200)

@click.group()
def cli():
    """
    Click group commands.
    """
    pass


@click.command()
@click.option("--port", default=5000,
              help="Listening port of the HTTP Test DANE.")
def run(port):
    """
    Run the SAND server and listen to port 'port'.
    """
    print "=============== HTTP Test DANE ================"
    print "-----------------------------------------------"
    import os
    if os.environ.get('PORT') is not None:
        port = int(os.environ['PORT'])
    APP.run(port=port)

cli.add_command(run)

if __name__ == '__main__':
    cli()
