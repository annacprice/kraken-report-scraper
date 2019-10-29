#!/usr/bin/env python3

import argparse
from csvbuilder import csvbuild

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-dir", dest="input", required=True, \
                        help = "path to the input directory")
    parser.add_argument("-o", "--output-dir", dest="output", required=True, \
                        help = "path to the output directory")

    args = parser.parse_args()
    input = args.input
    output = args.output
    csvbuild(input, output) 

if __name__ == "__main__":
    main()
