import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', default='Guest')
parser.add_argument('--age', default=18, type=int)
args = parser.parse_args()
print(f"Name: {args.name}, Age: {args.age}")
