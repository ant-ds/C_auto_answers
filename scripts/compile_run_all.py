#!/usr/bin/python3
import os
from os import path
import subprocess
from tqdm import tqdm

####
#  Configuration
####
# files where subprocess.run() seems to infinitely loop (python buffer issue?)
PROGRAM_HANGS = ["numerical_methods/gauss_elimination",
                 "data_structures/binary_trees/binary_search_tree",
                 "data_structures/binary_trees/threaded_binary_trees",
                 "data_structures/graphs/bfs",
                 "data_structures/graphs/dfs",
                 "data_structures/graphs/floyd_warshall",

                 ]

# files that don't seem to finish or are pointless to run
FAILING = ["client_server/server",  # Doesn't finish
           "client_server/udp_client",  # Doesn't finish
           "client_server/udp_server",  # Doesn't finish
           "data_structures/binary_trees/create_node",  # Empty main
           "data_structures/binary_trees/red_black_tree",  # Segmentation fault
           ]

# files that have a static main #TODO: fix
EMPTY = ["data_structures/binary_trees/segment_tree",
         "data_structures/graphs/transitive_closure"
         ]

# files that work with normal args (./foo 1 2 3) instead of scanf
NORMAL_ARGS = [("conversions/c_atoi_str_to_integer", [3])]

# TO_IGNORE = []

####
#  File find helper functions
####


def get_c_files(path, ignore_list=[]):
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
        if files[-2:].lower() == ".c" and files[2:-2].lower() not in ignore_list:
            c_files.append(files)
    # TODO: add skip files in ignorelist (that don't need to be compiled)

    # Return list of tuples: (complete path, filename)
    c_files.sort()
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


def get_out_files(path, ignore_list=[]):
    """
    Return a list of all out files (complete path, filename)
    """
    # Get all files in path
    all_files = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            all_files.append(os.path.join(root, name))

    # Keep only files ending in .c
    out_files = []
    for files in all_files:

        if files[-4:].lower() == ".out" and files[2:-4].lower() not in ignore_list:
            out_files.append(files)

    # Return list of tuples: (complete path, filename)
    out_files.sort()
    return(out_files)

####
#  Compile and run functions
####


def compile_files(c_files):
    """
    Compiles all given c_files
    Returns list of all .out paths
    """
    # TODO: deal with cmakes
    all_output_paths = []
    for path in tqdm(c_files, "Compiling..."):
        # Create output path
        output_path = path[:-2] + ".out"

        # Compile to output
        proc = subprocess.run(
            f"gcc -O2 -lm -o {output_path} {path}".split(), capture_output=True)
        # TODO: count amount of times compilation fails
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
            input_file), f"{input_file} doesn't exist!"
        proc = subprocess.run(
            f"./{path} < {input_file}".split(), stdin=subprocess.PIPE, shell=True, capture_output=True)
        # print(proc.stdout)


def main():
    programs_to_ignore = PROGRAM_HANGS + \
        FAILING + [idx[0] for idx in NORMAL_ARGS]
    print(programs_to_ignore)
    run_path = '.'
    c_files = get_c_files(path=run_path, ignore_list=programs_to_ignore)
    # out_files = compile_files(c_files=c_files)
    out_files = get_out_files(path=run_path, ignore_list=programs_to_ignore)
    run_all(paths=out_files)


if __name__ == "__main__":
    main()
