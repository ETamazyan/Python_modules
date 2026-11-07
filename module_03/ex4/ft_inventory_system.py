#!/usr/bin/env python3

import sys


def ft_split(text: str, separator: str) -> tuple[str, str] | None:
    first_part = ""
    current = ""
    found_separator = False
    i = 0

    if separator == "":
        return None

    while i < len(text):
        if text[i:i + len(separator)] == separator:
            if found_separator:
                return None

            found_separator = True
            i += len(separator)
        else:
            if found_separator:
                current += text[i]
            else:
                first_part += text[i]

            i += 1

    if not found_separator or first_part == "" or current == "":
        return None

    return first_part, current


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = {}
    for parameter in sys.argv[1:]:
        parts = ft_split(parameter, ":")
        if parts is None:
            print(f"Error - invalid parameter '{parameter}'")
            continue

    item_name = parts[0]
    quantity_text = parts[1]

    quantity = 0
    valid_quantity = True
    digit = 1
    for char in quantity_text:
        quantity = quantity * 10 + digit



# to run the programm
# python3 ft_inventory_system.py sword:1 potion:5 shield:2
