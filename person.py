import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name')
parser.add_argument('-a', '--age', type=int)
args = parser.parse_args()
print(f"Name: {args.name}, Age: {args.age}")