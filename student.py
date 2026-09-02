import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default='Unknown')
parser.add_argument('--age', type=int, default=18)
parser.add_argument('--course', type=str, default='Undecided')
args = parser.parse_args()
print(f"Name: {args.name}, Age: {args.age}, Course: {args.course}")
