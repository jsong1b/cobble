#!/usr/bin/env python3

# A simple Python script to bootstrap Cobble.
# Turns Markdown documents into source code.


import re
import sys


def main():
    if len(sys.argv) < 2:
        print('Not enough arguments')
        sys.exit(1)

    blocks = []
    for arg in sys.argv[1:]:
        (err, file_blocks) = extract_blocks(arg)
        if err != None:
            print(f'Could not extract blocks from file "{arg}": {err}', file = sys.stderr)
            continue
        blocks += [file_blocks]

    print(blocks)


class source_block:
    def __init__(self, origin = '', export = None, name = '', lines = []):
        self.origin = origin
        self.export = export
        self.name = name
        self.lines = lines


def extract_blocks(file_path):
    file_lines = []
    try:
        with open(file_path, 'r') as file:
            file_lines = [line.rstrip() for line in file]
    except Exception as e:
        return(str(e), None)

    blocks = []
    cur_block = source_block(origin = file_path)
    parser_state = None
    for line in file_lines:
        if ((parser_state == None and not re.match(r'^((`.+`)|\[.+\]\(.+\)):$', line)) or
            (parser_state == 'Named' and not re.match(r'^```.*$', line))):
            continue

        if parser_state == None and re.match(r'^((`.+`)|\[.+\]\(.+\)):$', line):
            if re.match(r'^`.+`:$', line):
                cur_block.name = line[1:-2]
            else:
                match = line.split('](')
                cur_block.export = match[0][1:]
                cur_block.name = match[1][:-2]

            parser_state = 'Named'
            continue

        if parser_state == 'Named' and re.match(r'^```.*$', line):
            parser_state = 'In Block'
            continue

        if parser_state == 'In Block' and re.match(r'^```$', line):
            blocks += [cur_block]
            cur_block = source_block(origin = file_path)
            parser_state = None
            continue

        if not parser_state == 'In Block':
            continue

        cur_block.lines += [line]


    return (None, blocks)


if __name__ == '__main__':
    main()
