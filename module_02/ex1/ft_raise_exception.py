#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    num_of_str = int(temp_str)
    # print(f"{num_of_str}")
    if num_of_str > 40:
        raise ValueError(f"{num_of_str}°C is too hot for plants (max 40°C)")
    if num_of_str < 0:
        raise ValueError(f"{num_of_str}°C is too cold for plants (min 0°C)")
    return num_of_str


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    try:
        print("\nInput data is 'abc'")
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    try:
        print("\nInput data is '100'")
        temperature = input_temperature("100")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    try:
        print("\nInput data is '-50'")
        temperature = input_temperature("-50")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")


if __name__ == "__main__":
    # num = input_temperature("55")
    # print(num)
    # print(type(num))

    print("=== Garden Temperature ===")
    # test_inputs = ["25", "abc"]

    # for temp_str in test_inputs:
    #     print(f"\nInput data is '{temp_str}'")
    test_temperature()

    print("\nAll tests completed - program didn't crash!")

# just the only improvement available
# def test_temperature() -> None:
#     test_inputs = ["25", "abc", "100", "-50"]

#     for temp_str in test_inputs:
#         try:
#             print(f"\nInput data is '{temp_str}'")
#             temperature = input_temperature(temp_str)
#             print(f"Temperature is now {temperature}°C")
#         except ValueError as error:
#             print(f"Caught input_temperature error: {error}")
