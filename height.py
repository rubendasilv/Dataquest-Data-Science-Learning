import argparse

parser = argparse.ArgumentParser()
parser.add_argument("height", type=float)

tall = parser.parse_args()
print(f"Your height in cm is: {tall.height}")
print(f"Your height in metres is: {tall.height * 0.01}")

