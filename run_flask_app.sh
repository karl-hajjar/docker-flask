#!/bin/bash

source env/bin/activate

echo "Port argument passed to bash script :"
echo $1

echo "Host argument passed to bash script :"
echo $2

python3 main.py --port=$1 --host=$2
