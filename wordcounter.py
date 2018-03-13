"""
Counts lines, words, characters and e-mail addresses

Uses three 'Counter' objects to:
1. Find the most common words in a given text file (a Counter type object)
2. Find all email addresses in that file (re module for regular expressions)
3. Count all the lines, words, characters and e-mails

Argument:
file        the name of the file to be parsed

Options:
-w          print the word count
-mc         print the most common words - 5 by default
-A          print all the words - with counter
-E          print all the e-mails
"""


import os
import re
import argparse
import sys
from collections import Counter


def count_mails(content):

    # Use regular expression to define search pattern
    pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    matches = pattern.findall(content)

    # Return a two element tuple - number of e-mails and list of e-mails
    return len(matches), matches


def count_words(content):

    # Find every string that starts with a letter
    pattern = re.compile(r'[a-zA-Z]\w*')  # should start with a letter followed by 0 or more word characters (a-z, A-Z, 0-9, _)
    matches = pattern.findall(content)

    # Return a list of words
    return matches


def count_else(file_name):

    # Count words - everything separated by spaces
    # Count lines - every line
    # Count nonemply lines
    # Count characters
    w_count, l_count, nl_count, c_count = 0, 0, 0, 0

    with open(file_name) as content:
        for line in content:
            l_count += 1
            c_count += len(line)
            line = line.strip()
            if line:
                w_count += len(line.split())
                nl_count += 1  # nonempty lines

    return l_count, nl_count, w_count, c_count  # return a tuple


def start(file_name):
    master_cnt = Counter(lines=0, n_lines=0, words=0, chars=0, mails=0)
    word_cnt = Counter()
    mail_cnt = Counter()

    with open(f'{file_name}', 'r') as in_file:
        content = in_file.read()

        # Counting e-mails
        master_cnt['mails'], mails = count_mails(content)
        mail_cnt = Counter(mails)

    with open(f'{file_name}', 'r') as in_file:
        content = in_file.read()

        # Counting words
        word_cnt = Counter(count_words(content))

    # Counting everything else
    master_cnt['lines'], master_cnt['n_lines'], master_cnt['words'], master_cnt['chars'] = count_else(file_name)

    return master_cnt, word_cnt, mail_cnt


def main():
    parser = argparse.ArgumentParser()
    pgroup = parser.add_mutually_exclusive_group()

    pgroup.add_argument('-w', '--words', help='print the word count', action='store_true')
    pgroup.add_argument('-mc', '--most_common', help='print the most common words - 5 by default', action='store_true')
    pgroup.add_argument('-A', '--all', help='print all the words - with counter', action='store_true')
    pgroup.add_argument('-E', '--emails', help='print all the e-mails', action='store_true')

    parser.add_argument('file', help='the name of the file to be parsed', type=str)

    args = parser.parse_args()

    assert os.path.isfile(args.file), 'FILE NOT FOUND'

    master_cnt, word_cnt, mail_cnt = start(args.file)

    if args.most_common:
        print('most common words')
        for w, c in word_cnt.most_common(5):
            print(f'"{w}" {c}')

    elif args.words:
        print(f"{master_cnt['words']} words")

    elif args.emails:
        for e in mail_cnt.keys():
            print(e)
        if not len(mail_cnt):
            print('no e-mails found')

    elif args.all:
        print('all the words')
        for w, c in word_cnt.most_common(len(word_cnt)):
            print(f'"{w}" {c}')

    else:
        print(f"{master_cnt['lines']} lines,", end=' ')
        print(f"{master_cnt['n_lines']} nonempty lines,", end=' ')
        print(f"{master_cnt['words']} words,", end=' ')
        print(f"{master_cnt['chars']} characters,", end=' ')
        print(f"{master_cnt['mails']} e-mails", end='\n')


if __name__ == '__main__':
    main()
