#!/usr/bin/env sh

cd "$(dirname $(realpath $0))"
../bootstrap/bootstrap.py *.md

sleep 0.1
echo "hello"
