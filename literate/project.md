# Project Setup

Here is how `Cobble` is used to convert documents to source code:
```txt
+-----------------------+
| Some kind of document |
+-----------+-----------+
            |
            | Frontend 
            ↓
       +---------+
       | TOML IR |
       +---------+
            |
            | Cobble (The Backend)
            ↓
  +-------------------+
  | Source code files |
  +-------------------+
```

The frontend can be any program that outputs the TOML IR to `stdout` or to a
file. `Cobble` is actually the backend, taking in TOML IR from a file or
`stdin` to produce source code files.

## Build Script

This is just a basic build script that (for now) calls the bootstrapper on all
the Markdown documents in `literate/` and builds the Go projects.

[build.sh](build.sh):
```sh
#!/usr/bin/env sh

cd "$(dirname $(realpath $0))"
sleep 0.05
../bootstrap/bootstrap.py *.md

<<<Build Cobble@cobble.md>>>
```
