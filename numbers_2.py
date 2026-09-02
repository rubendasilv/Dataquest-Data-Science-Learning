from statistics import mean
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--numbers', nargs='+', type=int, required=True)
args = parser.parse_args()
count = len(args.numbers)
total = sum(args.numbers)
avg = mean(args.numbers)

print(f"Numbers: {args.numbers}")
print(f"Count: {count}")
print(f"Total: {total}")
print(f"Average: {avg}")
