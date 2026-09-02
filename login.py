import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True)
args = parser.parse_args()
print(f"Welcome, {args.username}")