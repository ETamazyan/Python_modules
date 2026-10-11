#!/usr/bin/env python3

def input_temperature(temp_str) -> int:
    num_of_str = int(temp_str)
    # print(f"{num_of_str}")
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

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    # num = input_temperature("55")
    # print(num)
    # print(type(num))

    print("=== Garden Temperature ===")
    # test_inputs = ["25", "abc"]

    # for temp_str in test_inputs:
    #     print(f"\nInput data is '{temp_str}'")

    test_temperature()
