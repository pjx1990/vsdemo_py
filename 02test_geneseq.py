#! /usr/bin/env python3
import argparse
import random
from typing import NamedTuple, TextIO

class Args(NamedTuple):
    seq_len: int
    num_seqs: int
    out_file: TextIO

def get_args() -> Args:
    parse = argparse.ArgumentParser(
        description='generate long seq',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parse.add_argument('-l','--len',help='seq len',metavar='int',type=int,default=1000000)
    parse.add_argument('-n','--num',help='num of seq',metavar='int',type=int,default=100)
    parse.add_argument('-o','--outfile',help='outfile',metavar='FILE',type=argparse.FileType('wt'),default='seq.txt')
    args = parse.parse_args()

    return Args(args.len, args.num, args.outfile)

def main() -> None:
    args = get_args()
    for _ in range(args.num_seqs):
        print(''.join([random.choice('ACGT') for _ in range(args.seq_len)]),
        file=args.out_file)
    print(f'Done, see "{args.out_file.name}".')

if __name__ == '__main__':
    main()
