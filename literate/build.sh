#!/usr/bin/env sh

cd "$(dirname $(realpath $0))"
sleep 0.05
../bootstrap/bootstrap.py *.md

cd "$(dirname $(realpath $0))/../cobble"
sleep 0.05
go mod tidy
go build -o cobble cobble.go
