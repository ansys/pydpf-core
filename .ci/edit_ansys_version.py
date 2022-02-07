import sys
import pkgutil
import os

if __name__ == "__main__":
    directory = os.path.dirname(pkgutil.get_loader("ansys.dpf.core").path)
    file_path = os.path.join(directory, "_version.py")
    for i, arg in enumerate(sys.argv):
        if arg == "--version":
            print(sys.argv[i+1])
            version = sys.argv[i+1]
    file = open(file_path, 'r')
    lines = file.readlines()
    for i, line in enumerate(lines):
        if "__ansys_version__" in line:
            lines[i] = f'__ansys_version__ = "{version}"\n'
    file.close()
    with open(file_path, 'w') as file:
        file.writelines(lines)
