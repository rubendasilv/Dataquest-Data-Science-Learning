import argparse

parser = argparse.ArgumentParser(description="A command-line toolkit for managing and inspecting software projects.")

subparsers = parser.add_subparsers(dest='command',required=True, help='Available commands')

init_parser = subparsers.add_parser('init', help='create a new project')
inspect_parser = subparsers.add_parser('inspect', help='inspect project structure')
stats_parser = subparsers.add_parser('stats', help='display project statistics')
test_parser = subparsers.add_parser('test', help='run project tests')
clean_parser = subparsers.add_parser('clean', help='remove generated project files')
git_parser = subparsers.add_parser('git', help='perform Git related operations')


git_subparsers = git_parser.add_subparsers(dest='git_command', help='Git related operations')

status_parser = git_subparsers.add_parser('status')

log_parser = git_subparsers.add_parser('log')
