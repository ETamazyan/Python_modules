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

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        quantity = 0
        valid_quantity = True

        for char in quantity_text:
            if char == "0":
                digit = 0
            elif char == "1":
                digit = 1
            elif char == "2":
                digit = 2
            elif char == "3":
                digit = 3
            elif char == "4":
                digit = 4
            elif char == "5":
                digit = 5
            elif char == "6":
                digit = 6
            elif char == "7":
                digit = 7
            elif char == "8":
                digit = 8
            elif char == "9":
                digit = 9
            else:
                valid_quantity = False
                break

            quantity = quantity * 10 + digit

        if not valid_quantity:
            print(
                f"Quantity error for '{item_name}': "
                f"invalid literal for int() with base 10: '{quantity_text}'"
            )
            continue

        inventory[item_name] = quantity

    print("Got inventory:", inventory)

    # Creating item list
    item_list = list(inventory.keys())
    print("Item list:", item_list)

    # Calculate total quantity
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    if total_quantity > 0:
        for item in inventory.keys():
            percentage = round(
                inventory[item] / total_quantity * 100, 1
            )
            print(f"Item {item} represents {percentage}%")

    if len(item_list) > 0:
        most_abundant = item_list[0]
        least_abundant = item_list[0]

        for item in item_list:
            if inventory[item] > inventory[most_abundant]:
                most_abundant = item

            if inventory[item] < inventory[least_abundant]:
                least_abundant = item
        print(
            f"Item most abundant: {most_abundant} "
            f"with quantity {inventory[most_abundant]}"
        )

        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {inventory[least_abundant]}"
        )
    else:
        print("Inventory is empty")

    # Add a new item
    new_item = "magic_item"

    if new_item in inventory:
        new_item = "rare_gem"

    if new_item in inventory:
        new_item = "ancient_scroll"

    if new_item not in inventory:
        inventory.update({new_item: 1})

    print("Updated inventory:", inventory)


# to run the programm
# python3 ft_inventory_system.py sword:1 potion:5 shield:2
# or
# python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3
# helmet:1 sword:2 hello key:value