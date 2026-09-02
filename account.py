import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--username', type=str, required=True)
def valid_age(value):
    age = int(value)
    if age < 18 or age > 100:
        raise argparse.ArgumentTypeError(f"Age must be between 18 and 100")
    return age
parser.add_argument('--age', type=valid_age, required=True)
parser.add_argument('--role', choices=['admin', 'user', 'guest'], default='user')
args = parser.parse_args()
print(f"Username: {args.username}, Age: {args.age}, Role: {args.role}")
