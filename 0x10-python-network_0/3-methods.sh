#!/bin/bash
#show all allowed methods
curl -sI $1 | grep "Allow"
