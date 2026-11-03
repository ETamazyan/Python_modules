#!/usr/bin/env python3

import math

print(math.sqrt(4))


def ft_split(text: str, separator: str) -> tuple[float, float, float] | None:
    result = []
    current = ""
    i = 0

    if separator == "":
        raise ValueError("Empty separator")

    while i < len(text):
        if text[i:i + len(separator)] == separator:
            try:
                result.append(float(current))
            except ValueError as error:
                print(f"Error on parameter '{current.strip()}': {error}")
                return None

            current = ""
            i += len(separator)
        else:
            current += text[i]
            i += 1

    try:
        result.append(float(current))
    except ValueError:
        print("Invalid syntax")
        return None

    return tuple(result)


def get_player_pos() -> list[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        coordinates = ft_split(user_input, ",")

        if coordinates is None:
            # print("Invalid coordinates")
            continue

        if len(coordinates) != 3:
            print("Invalid syntax: enter exactly three coordinates")
            continue

        return coordinates


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")

    position1 = get_player_pos()

    print(f"Got a first tuple: {position1}")
    print(f"It includes: X={position1[0]}, Y={position1[1]}, Z={position1[2]}")

    distance = math.sqrt(
        position1[0] ** 2
        + position1[1] ** 2
        + position1[2] ** 2
    )

    print(f"Distance to center: {round(distance, 4)}")
    print("")
    print("Get a second set of coordinates")

    position2 = get_player_pos()
    distance = math.sqrt(
        (position2[0] - position1[0]) ** 2
        + (position2[1] - position1[1]) ** 2
        + (position2[2] - position1[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")
