"""Here we write all the doc string examples. This way we can be sure that they
still work.
A method is written for each python file of dpf-core.
If a failure occurs, the change must be done here and in the corresponding
docstring."""

import doctest
import os
import pathlib

import pytest


@pytest.mark.skipif(True, reason="examples are created for windows")
def test_doctest_allfiles():
    directory = r"../ansys/dpf/core"
    actual_path = pathlib.Path(__file__).parent.absolute()
    # actual_path = os.getcwd()
    print(actual_path)
    for filename in os.listdir(os.path.join(actual_path, directory)):
        if filename.endswith(".py"):
            path = os.path.join(directory, filename)
            print(path)
            doctest.testfile(path, verbose=True, raise_on_error=True)
        else:
            continue


@pytest.mark.skipif(True, reason="examples are created for windows")
def test_doctest_allexamples():
    directory = r"../examples"
    actual_path = pathlib.Path(__file__).parent.absolute()
    handled_files = []
    for root, subdirectories, files in os.walk(os.path.join(actual_path, directory)):
        for subdirectory in subdirectories:
            subdir = os.path.join(root, subdirectory)
            print(subdir)
            for filename in os.listdir(subdir):
                if filename.endswith(".py"):
                    path = os.path.join(subdir, filename)
                    if ".ipynb_checkpoints" in path:
                        continue
                    print(path)
                    handled_files.append(path)
                    exec(
                        open(path, mode="r", encoding="utf8").read(),
                        globals(),
                        globals(),
                    )
                else:
                    continue
    print(handled_files)


if __name__ == "__main__":
    test_doctest_allfiles()
