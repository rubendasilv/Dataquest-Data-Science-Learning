import argparse

def valid_age(value):
    age = int(value)
    if age < 0 or age > 120:
        raise argparse.ArgumentTypeError(f"Age must be between 0 and 120")
    else:return age
parser = argparse.ArgumentParser()
parser.add_argument('--age', type=valid_age)
args = parser.parse_args()
print("Age:", {args.age})
