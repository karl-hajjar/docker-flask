#!/bin/bash

if [ -z "$1" ]; then port=5000; else port=$1; fi

echo "POST request being sent to port $port"
echo "Full POST command :"
echo "-X POST http://localhost:$port/action/123456"

curl -X POST http://localhost:$port/action/123456