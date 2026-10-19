#!/usr/bin/env python3

import sys

# slicing is not recomended enumerate()
# for i, arg in enumerate(sys.argv[1:], start=1):
#     print(f"Argument {i}: {arg}")

# args to use only users arguments
# args = sys.argv[1:]

# some texte fhdeirernhivgwpdfgvief
if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")

        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {len(sys.argv)}")
