from pathlib import Path 

company = Path("company")
software =  company /  "software"
backend = software / "backend"
database = backend / "database"
models = database / "models"
user = models / "user.py"

print(company)
print(software)
print(backend)
print(database)
print(models)
print(user)