#!/bin/bash
#curl a url and et conten-length value
curl -i $1 |  grep 'Content-Length:' | cut -d " " -f 2
