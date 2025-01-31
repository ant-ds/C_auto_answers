# The Algorithms - C - Auto-answers

This fork of [The Algorithms](https://github.com/TheAlgorithms/C) containing needed input files to automatically run all files when compiled.
The purpose of this repo is to help in automatically constructing datasets of C file traces.

It does so by providing an input file for every C file that fills in all required input. 

## How auto-running works
This is an example for file `foo.c`:
 1. Compile the file: `gcc -O2 foo.c -O foo.out`
 2. Run it with given input: `./foo.out < foo.input`

 For full automatisation, take a look at the python scripts in the `scripts` directory.
 
 Run: `./scripts/compile_run_all.py`

 (This script was only tested on a machine running Ubuntu 20.04)
 
## The Algorithms - C
### Overview

The repository is a collection of open-source implementation of a variety of algorithms implemented in C and licensed under [GPLv3 License](https://github.com/TheAlgorithms/C/blob/master/LICENSE). The algorithms span a variety of topics from computer science, mathematics and statistics, data science, machine learning, engineering, etc.. The implementations and the associated documentation are meant to provide a learning resource for educators and students. Hence, one may find more than one implementation for the same objective but using a different algorithm strategies and optimizations.

### Features

* The repository provides implementations of various algorithms in one of the most fundamental general purpose languages - [C](https://en.wikipedia.org/wiki/C_(programming_language)).
* Well documented source code with detailed explanations provide a valuable resource for educators and students alike.
* Each source code is atomic using standard C library [`libc`](https://en.wikipedia.org/wiki/C_standard_library) and _no external libraries_ are required for their compilation and execution. Thus the fundamentals of the algorithms can be studied in much depth.
* Source codes are [compiled and tested](https://github.com/TheAlgorithms/C/actions?query=workflow%3A%22Awesome+CI+Workflow%22) for every commit on the latest versions of three major operating systems viz., Windows, MacOS and Ubuntu (Linux) using MSVC 16 2019, AppleClang 11.0 and GNU 7.5.0 respectively.
* Strict adherence to [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)) standard ensures portability of code to embedded systems as well like ESP32, ARM Cortex, etc. with little to no changes.
* Self-checks within programs ensure correct implementations with confidence.
* Modular implementations and OpenSource licensing enable the functions to be utilized conveniently in other applications.

### Documentation

[Online Documentation](https://TheAlgorithms.github.io/C) is generated from the repository source codes directly. The documentation contains all resources including source code snippets, details on execution of the programs, diagrammatic representation of program flow, and links to external resources where necessary.
Click on [Files menu](https://TheAlgorithms.github.io/C/files.html) to see the list of all the files documented with the code.

[Documentation of Algorithms in C](https://thealgorithms.github.io/C) by [The Algorithms Contributors](https://github.com/TheAlgorithms/C/graphs/contributors) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1)<br/>
<a href="https://creativecommons.org/licenses/by-sa/4.0"><img alt="Creative Commons License" style="height:22px!important;margin-left: 3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" /><img  alt="Credit must be given to the creator" style="height:22px!important;margin-left: 3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg" /><img alt="Adaptations must be shared under the same terms" style="height:22px!important;margin-left: 3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" /></a>

### Contributions

As a community developed and maintained repository, we welcome new un-plagiarized quality contributions. Please read our [Contribution Guidelines](https://github.com/TheAlgorithms/C/blob/master/CONTRIBUTING.md).
