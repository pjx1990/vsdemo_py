#! /usr/bin/env python3
""" transcribe dna into rna """

import argparse
import os
from typing import NamedTuple, List, TextIO

class Args(NamedTuple):
    '''command line arguments'''
    files: List[TextIO]
    out_dir: str

def get_args() -> Args:
    '''gent command line arguments'''
    parse = argparse.ArgumentParser(description='transcribe dna into rna',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parse.add_argument('file',help='input dna file(s)',metavar="FILE",type=argparse.FileType('rt'),nargs='+')
    parse.add_argument('-o','--out_dir',help='out directory',metavar='DIR',type=str,default='out')

    args = parse.parse_args()
    return Args(args.file, args.out_dir)

def main() -> None:
    args = get_args()
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    num_files, num_seqs = 0, 0
    for fh in args.files:
        num_files += 1
        out_file = os.path.join(args.out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')

        for dna in fh:
            num_seqs += 1
            out_fh.write(dna.replace('T', 'U'))
        out_fh.close()

    print(f'Done, wrote {num_seqs} sequence{"" if num_seqs == 1 else "s"} '
        f'in {num_files} file{"" if num_files == 1 else "s"} '
        f'to directory "{args.out_dir}".')

if __name__ == '__main__':
    main()