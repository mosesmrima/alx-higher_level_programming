#!/usr/bin/python3
""" cript that fetches https://intranet.hbtn.io/status """

import urllib.request

req = urllib.request.Request("https://intranet.hbtn.io/status")
with urllib.request.urlopen(req) as res:
    body = res.read()
    print("Body response:")
    print("\t - type: {}".format(type(body)))
    print("\t - content: {}".format(body))
    print("\t - utf8 content: {}".format(body.decode("utf-8")))
