#!/bin/bash

source env/bin/activate

echo "Port argument passed to bash script :"
echo $1
host="0.0.0.0"
echo "Host argument passed to python script:"
echo $host
python3 main.py --port=$1 --host=$host
