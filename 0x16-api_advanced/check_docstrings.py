#!/usr/bin/python3
import importlib.util
import os
import sys

def check_module_docstrings(path):
    """
    Checks all Python modules in the specified directory or a single file for documentation.
    """
    if os.path.isfile(path):
        files = [path]
    else:
        files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.py')]

    for filename in files:
        module_name = os.path.splitext(os.path.basename(filename))[0]
        try:
            spec = importlib.util.spec_from_file_location(module_name, filename)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            docstring = module.__doc__
            if docstring:
                print(f"Module '{module_name}' has documentation.")
                print(f"Documentation:\n{docstring}\n")
            else:
                print(f"Module '{module_name}' is missing documentation.")
        except Exception as e:
            print(f"Failed to import module '{module_name}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 check_docstrings.py <directory_or_file>")
        sys.exit(1)
    
    path = sys.argv[1]
    check_module_docstrings(path)
