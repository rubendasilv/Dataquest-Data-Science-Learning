import argparse

parser = argparse.ArgumentParser(
    description="A simple calculator that peforms addition, subtraction and multiplication on three numbers.")
parser.add_argument('--add', type=int, nargs=2, help="Add maximum of two numbers")
parser.add_argument('--subtract', type=int, nargs=2, help='Subtract maximum of two numbers')
parser.add_argument('--multiply', type=int, nargs=2, help='Multiply maximum of two numbers')
args = parser.parse_args()

if args.add:
    print(f"Addition: {args.add[0] + args.add[1]}")
if args.subtract:
    print(f"Subtraction: {args.subtract[0] - args.subtract[1]}")
if args.multiply:
    print(f"Multiplication: {args.multiply[0] * args.multiply[1]}")