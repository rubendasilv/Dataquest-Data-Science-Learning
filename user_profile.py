import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', type=str, default='Unknown')
parser.add_argument('-a', '--age', type=int, default=18)
parser.add_argument('--height', type=float, default=170.0)
args = parser.parse_args()
print(f"Name: {args.name}, Age: {args.age}, Height: {args.height} cm")
height_m = args.height * 0.01
print(f"Height: {height_m} m")