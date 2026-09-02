import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--level', default='beginner', choices=['beginner', 'intermediate', 'advanced'])
args = parser.parse_args()
print(f"level: {args.level}")
