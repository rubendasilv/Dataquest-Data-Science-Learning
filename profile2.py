import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--age', type=int, required=True)
parser.add_argument('-verbose', action='store_true')
args = parser.parse_args()
if args.verbose:
    print(f'Name: {args.name}, Age: {args.age}, Verbose mode is on: {args.verbose}')
else:
    print(f'Name: {args.name}, Age: {args.age}, Verbose mode is off: {args.verbose}')
