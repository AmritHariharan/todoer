#!/usr/bin/env python

# TODOER
# By: Amrit Hariharan
# Python comment parser and todo list generator

import re
from sys import exit
from sys import argv

if __name__ == "__main__":

    output_file = ''
    # Check arguments
    if (len(argv) == 2):
        output_file = 'output.md'
    elif (len(argv) == 3):
        output_file = argv[2]
        if output_file[output_file.find('.'):] != '.md':
            print("Usage: $ python todoer.py INPUT_FILE (OUTPUT_FILE.md)")
            sys.exit(0)
    else:
        print("Usage: $ python todoer.py INPUT_FILE (OUTPUT_FILE.md)")
        sys.exit(0)

    # Dictionary of all todo items
    keywords = [
        'TODO:',
        'FIXME:',
        'WTF:',
    ] # Add keywords here
    todos = dict((keywords[i], []) for i in range(len(keywords)))

    # Find out what comment syntax was used
    comment_types = {
        'cpp': '//',        # C++
        'c': '//',	    # C
        'java': '//',       # Java
        'js': '//',	    # JavaScript
        'py': '#',	    # Python
        'sh': '#',	    # Bash shell scripts
        'hs': '--',	    # Haskell
        'lhs': '--',        # Haskell
    } # Add languages here

    # Get block comment regex
    block_comment_regex = {
            '//': '\/\*[^\/\*]+(TODO)[^\*\/]+\*\/'
            } # Regex to catch block comments of the form /* comment \n\n lines */

    filename = argv[1]
    comment = comment_types[filename[filename.find('.')+1:]]
    expression = block_comment_regex[comment]
    #print('comment syntax: %s this is a line comment' % comment)

    # Go through the file line by line
    line_num = 1
    with open(argv[1], 'r') as f:
        # TODO: make this more concise if possible
        for line in f:
            pos = line.find(comment)
            if pos != -1:
                for tag in keywords:
                    tag_pos = line.find(tag)
                    if tag_pos != -1:
                        todos[tag].append((line_num, line[tag_pos+len(tag):-1]))
            line_num += 1

    # Print out all relevant comments
    print('# Todo list for `%s`\n-----' % filename, file=open(output_file, 'w'))
    for tag in keywords:
        if todos[tag]:
            print('## %s' % tag, file=open(output_file, 'a'))
            for line in todos[tag]:
                print('- [ ] line %d: %s' % (line[0], line[1]), file=open(output_file, 'a'))
                print('-----', file=open(output_file, 'a'))

    print('todo list for %s saved in %s' % (filename, output_file))
