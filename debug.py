import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()
print(f"Debug mode enabled: {args.debug}")
