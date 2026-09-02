import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()
if args.verbose:
    print(f"Hello, {args.name}! Verbose mode is on.")
else:
    print(f"Hello, {args.name}! Verbose mode is off.")
