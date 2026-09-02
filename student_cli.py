import argparse

def valid_age(value):
    age = int(value)
    if age < 18 or age > 100:
        raise argparse.ArgumentTypeError(f"Age must be between 18 and 100")
    return age

parser = argparse.ArgumentParser(description='Student management CLI')

#prevents execution without subcommand
subparsers = parser.add_subparsers(dest='command')

parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

add_parser = subparsers.add_parser('add')
list_parser = subparsers.add_parser('list')
remove_parser = subparsers.add_parser('remove')
update_parser = subparsers.add_parser('update')

add_parser.add_argument('--name', type=str, required=True, help='Name of the student to add')
add_parser.add_argument("--age", type=valid_age, required=True, help='Age of the student')
add_parser.add_argument("--course", type=str, required=True, help='Course of the student')

list_parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

remove_parser.add_argument('id', type=str, help='ID of the student to remove')
update_parser.add_argument('student', type=str, help='Name of the student to update')

#required arguments with custom validation for age



args = parser.parse_args()

#Print statment for verbose flag
if args.verbose:
    print(f"Verbose mode is on")
else:
    print(f"Verbose mode is off")

if args.command == 'add':
    print("Added:", args.name)
elif args.command == 'list':
    print("Showing all students...", args.list)
elif args.command == 'remove':
    print("Removing...", args.id)
elif args.command == 'update':
    print("Updating...", args.update)


