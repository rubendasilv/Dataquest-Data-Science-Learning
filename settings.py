import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('--verbose', action='store_true')
group.add_argument('--quiet', action='store_true')
args = parser.parse_args()
print(f"Verbose mode: {args.verbose}, Quiet mode: {args.quiet}")