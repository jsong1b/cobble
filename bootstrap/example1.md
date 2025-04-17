# Example Literate Document

This is a simple example literate document.

[test1.txt](test1.txt):
```txt
This is an example file showcasing how Cobble exports

<<<Example Block 1>>>

prefix: <<<Example Block 1>>>

<<<Example Block 2@example2.md>>> :suffix
```

[test2.txt](test2.txt):
```txt
<<<test1.txt>>>

prefix: <<<test1.txt>>> :suffix
```

`Example Block 1`:
```txt
This is an example block that is not exported to a file.
```
