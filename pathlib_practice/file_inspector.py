from pathlib import Path 

workspace = Path("workspace")
workspace.mkdir()

main = workspace / "main.py" #connects file to workspace
main.touch(exist_ok=True) # Creates main.py file

config = workspace / "config.JSON"#connects to workspace
config.touch()#creates file

data = workspace / "data"
data.mkdir()

sales = data / "sales.csv"
sales.touch()

users = data / "users.csv"
users.touch()

src = workspace / "src"
src.mkdir()

calculator = src / "calculator.py"
calculator.touch()

utils = src / "utils.py"
utils.touch()

tests = workspace / "tests"
tests.mkdir()

test = tests / "test.py"
test.touch()

print("Workkspace exists: ", workspace.exists())

print("Content")
for item in workspace.iterdir():
    if item.is_dir():
        print("Directory", item.name)
    elif item.is_file():
        print("File", item.name)

print("python files:")
for file in workspace.rglob("*.py"):
    print(file.name)

print("csv files")
for file in workspace.rglob("*.csv"):
    print(file.name)