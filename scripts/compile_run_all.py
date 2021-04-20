#!/usr/bin/python3
import os
from os import path
import subprocess
from tqdm import tqdm

####
#  File find helper functions
####


def get_c_files(path):
    """
    Return a list of all c files (complete path)
    """
    # Get all files in path
    all_files = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            all_files.append(os.path.join(root, name))

    # Keep only files ending in .c
    c_files = []
    for files in all_files:
        if files[-2:].lower() == ".c":
            c_files.append(files)
    # TODO: add skip files in ignorelist (that don't need to be compiled)

    # Return list of tuples: (complete path, filename)
    return(c_files)


def get_directories(path):
    """
    Returns a list of all directories in given path
    """
    all_dirs = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in dirs:
            all_dirs.append(os.path.join(root, name))

    return all_dirs


def get_out_files(path):
    """
    Return a list of all out files (complete path, filename)
    """
    # Get all files in path
    all_files = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            all_files.append(os.path.join(root, name))

    # Keep only files ending in .c
    c_files = []
    for files in all_files:
        if files[-4:].lower() == ".out":
            c_files.append(files)
    # TODO: add skip files in ignorelist (that don't need to be compiled)

    # Return list of tuples: (complete path, filename)
    return(c_files)


def compile_files(c_files):
    """
    Compiles all given c_files
    Returns list of all .out paths
    """
    all_output_paths = []
    for path in tqdm(c_files, "Compiling..."):
        # Create output path
        output_path = path[:-2] + ".out"

        # Compile to output
        proc = subprocess.run(
            f"gcc -O2 -o {output_path} {path}".split(), capture_output=True)

        all_output_paths.append(output_path)

    return all_output_paths


def run_all(paths):
    """
    Runs all .out files specified in the list of paths
    """
    for path in tqdm(paths, "Running: "):
        # Check existence of .input file
        input_file = path[:-4] + ".input"
        assert os.path.isfile(
            input_file), f"{input_file} doesn't exist!\nPlease create this input file"
        proc = subprocess.run(
            f"./{path} < {input_file}".split(), capture_output=True)


def main():
    run_path = '.'
    c_files = get_c_files(path=run_path)
    out_files = compile_files(c_files=c_files)
    # out_files = get_out_files(path=run_path)
    run_all(paths=out_files)


if __name__ == "__main__":
    main()
