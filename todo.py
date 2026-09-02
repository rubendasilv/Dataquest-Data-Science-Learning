import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--task', action="append", choices=['Study Python', 'Study argparse', 'Build project'])
args = parser.parse_args()
print(f"""Tasks:
      1. {args.task[0]}
      2. {args.task[1]}
      3. {args.task[2]}""")