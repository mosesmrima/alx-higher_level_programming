#!/bin/bash
#set origin and data/user_id
curl -sX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
