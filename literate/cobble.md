# `Cobble`

This is the implementation of the actual `Cobble` program, which just takes in
an input of a special TOML IR and outputs source code files.

## Project Setup

Here are the `go.mod` and `cobble.go` files of the project. The project is
using Go because it's simple, can be cross compiled, and will make it easier to
parallize.

[../cobble/go.mod](../cobble/go.mod):
```go
module github.com/jsong1b/cobble

go 1.24.2
```

[../cobble/cobble.go](../cobble/cobble.go):
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, world!")
}
```

Here is what is expanded into [project.md](project.md) to build the backend.

`Build Cobble`:
```sh
cd "$(dirname $(realpath $0))/../cobble"
sleep 0.05
go mod tidy
go build -o cobble cobble.go
```

This will generate a binary at `../cobble/cobble`, which we don't want to show
up in the Git repo, so we need a `.gitignore`.

[../cobble/.gitignore](../cobble/.gitignore):
```gitignore
cobble
```
