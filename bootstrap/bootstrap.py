#!/usr/bin/env python3

# A simple Python script to bootstrap Cobble.
# Turns Markdown documents into source code.


import re
import sys


def main():
    if len(sys.argv) < 2:
        print('Not enough arguments')
        sys.exit(1)

    for arg in sys.argv[1:]:
        (err, blocks) = extract_blocks(arg)
        if err != None:
            print(f'Could not extract blocks from file "{arg}": {err}', file = sys.stderr)
            continue


def extract_blocks(file_path):
    file_lines = []
    try:
        with open(file_path, 'r') as file:
            file_lines = [line.rstrip() for line in file]
    except Exception as e:
        return(str(e), None)

    blocks = []
    parser_state = None
    for line in file_lines:
        # print(parser_state, line)

        if ((parser_state == None and not re.match(r'^((`.+`)|\[.+\]\(.+\)):$', line)) or
            (parser_state == 'Named' and not re.match(r'^```.*$', line))):
            continue

        if parser_state == None and re.match(r'^((`.+`)|\[.+\]\(.+\)):$', line):
            # naming the block
            parser_state = 'Named'
            print(line)
            continue

        if parser_state == 'Named' and re.match(r'^```.*$', line):
            # at start of block
            parser_state = 'In Block'
            continue

        if parser_state == 'In Block' and re.match(r'^```$', line):
            # save block
            parser_state = None
            continue

        if not parser_state == 'In Block':
            continue

        print(line)


    return (None, None)


if __name__ == '__main__':
    main()
