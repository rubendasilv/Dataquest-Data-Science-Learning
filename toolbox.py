import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

add_parser = subparsers.add_parser('add')
list_parser = subparsers.add_parser('list')
remove_parser = subparsers.add_parser('remove')
update_parser = subparsers.add_parser('update')

add_parser.add_argument('task', type=str)
list_parser.add_argument( type=str)
remove_parser.add_argument('task', type=str)
update_parser.add_argument('task', type=str)

args = parser.parse_args()

if args.command == 'add':
    print("Added:", args.task)
elif args.command == 'list':
    print("Showing all tasks...", args.task)
elif args.command == 'remove':
    print("Removing...", args.task)
elif args.command == 'update':
    print("Updating...", args.task)
