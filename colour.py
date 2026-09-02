import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--colour', choices=['red', 'green', 'blue'])
args = parser.parse_args()
print(f"Colour selected: {args.colour}")
