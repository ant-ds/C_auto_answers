#!/usr/bin/python3
import os
from os import path
import subprocess
from tqdm import tqdm


def get_c_files(path):
    """
    Return a list of all c files in format (complete path, filename)
    """
    # Get all files in path
    all_files = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            all_files.append((os.path.join(root, name), name))

    # Keep only files ending in .c
    c_files = []
    for files in all_files:
        if files[0][-2:].lower() == ".c":
            c_files.append(files)
    # TODO: add skip files in ignorelist (that don't need to be compiled)

    # Return list of tuples: (complete path, filename)
    return(c_files)


def get_all_directories(path):
    """
    Returns a list of all directories in given path
    """
    all_dirs = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in dirs:
            all_dirs.append(os.path.join(root, name))

    return all_dirs


def compile_files(file_tups):
    """
    Compiles all given files in destination path
    file_tups are tuples of format: (complete path, filename)
    Returns list of all output paths of .out files
    """
    all_output_paths = []
    for path, name in tqdm(file_tups, 'Compling...'):
        # Create output path
        output_path = path[:-2] + '.out'

        # Compile to output
        proc = subprocess.run(
            f"gcc -O2 -o {output_path} {path}".split(), capture_output=True)

        all_output_paths.append(output_path)

    return all_output_paths


def run_all(paths):
    """
    Runs all .out files specified in the list of paths
    """
    # TODO
    pass


def main():
    file_tups = get_c_files(path='.')
    out_files = compile_files(file_tups=file_tups)
    run_all(paths=out_files)


if __name__ == "__main__":
    main()
