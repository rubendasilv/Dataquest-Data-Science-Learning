from pathlib import Path
import shutil

#---- checks ----
def is_file(path):
    return path.is_file()
def is_dir(path):
    return path.is_dir()
def exists(path):
    return path.exists()

#----listing----
def list_files(path):
    file = []
    for item in path.iterdir():
        if item.is_file():
            file.append(item)
    return file

def list_dir(path):
    directory = []
    for item in path.iterdir():
        if item.is_dir():
              directory.append(item)
    return directory

#----read/write----
def read_file(path):
    return path.read_text()
def write_file(path, argument):
    return path.write_text(argument)

#---create---
def create_dir(path):
        return path.mkdir(exist_ok=True)
def create_file(path):
        return path.touch(exist_ok=True)

#---delete---
def delete_file(path):
    return path.unlink(missing_ok=True)
def delete_dir(path):
    if path.exists() and path.is_dir():
        return shutil.rmtree(path)

#---move---
def move_file(source, destination):
    return shutil.move(source, destination)



#---copy---
def copy_file(source, destination):
    return shutil.copy(source, destination)






