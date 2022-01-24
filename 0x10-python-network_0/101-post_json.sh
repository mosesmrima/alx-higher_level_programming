#!/bin/bash
#send data from a json file
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
