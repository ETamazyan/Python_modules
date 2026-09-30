class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age_days += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return
        self._age_days = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age_days


if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    pl1 = Plant("Rose", 15.0, 10)
    pl1.show()

    print("\n", end="")

    pl1.set_height(25)
    print(f"Height updated: {pl1.get_height()}cm")
    pl1.set_age(30)
    print(f"Age updated: {pl1.get_age()} days")

    print("\n", end="")

    pl1.set_height(-5)
    print("Height update rejected")
    pl1.set_age(-10)
    print("Age update rejected")

    print("\n", end="")

    print("Current state:", end=" ")
    pl1.show()
