#!/usr/bin/env python3


def ft_split(text: str, separator: str) -> tuple[float] | None:
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
        # print(f"Error on parameter '{current.strip()}': {error}")
        return None

    return tuple(result)


def get_player_pos() -> list[float]:
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

    position = get_player_pos()
    print("Player position:", position)

# #!/usr/bin/env python3

# # import math

# def ft_split(text: str, separator: str) -> list | None:
#     result = []
#     current = ""
#     i = 0
#     valid = True

#     if separator == "":
#         raise ValueError("Empty separator")
#     while i < len(text):
#         if text[i:i+len(separator)] == separator:
#             try:
#                 result.append(float(current))
#                 current = ""
#                 i += len(separator)
#             except ValueError as error:
#                 print(f"Error on parameter '{part.strip()}': {error}")
#                 valid = False
#                 break
#         else:
#             current += text[i]
#             i += 1
#     try:
#         result.append(current)
#     except ValueError as error:
#         print(f"Error on parameter '{result.strip()}': {error}")
#         valid = False
#     if valid:
#         return result


# def get_player_pos():
#     while True:
#         user_input = input(
#             "Enter new coordinates as floats in format 'x,y,z': "
#         )
#         print("Input received:", user_input)      # just keep
#         sep_input = ft_split(user_input, ",")

#         if len(sep_input) != 3 | sep_input is None:
#             print("Invalid syntax")    # try this or just raise an exception
#             continue


# if __name__ == "__main__":
#     print("=== Game Coordinate System ===\n")
#     print("Get a first set of coordinates")
#     get_player_pos()
