class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days
        print(f"Plant created: {self._name}")

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


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        color: str,
    ) -> None:
        super().__init__(name=name, height=height, age_days=age_days)
        self.color = color
    print("\n=== Flower")

    def bloom(self):
        print("[asking the rose to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        trunk_diameter: str,
    ) -> None:
        super().__init__(name=name, height=height, age_days=age_days)
        self.trunk_diameter = trunk_diameter
        print("\n=== Tree")

    def produce_shade(self):
        print("[asking the oak to produce shade]")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name=name, height=height, age_days=age_days)
        self.harvest_season = harvest_season
        self. nutritional_value = nutritional_value
        print("\n=== Vegetable")

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    rose = Flower(
        name="Rose",
        height=15.0,
        age_days=10,
        color="yellow",
    )

    rose.show()
    print("Rose has not bloomed yet")
    rose.bloom()
    rose.show()
    print("Rose is blooming beautifully!")

    oak = Tree(
        name="Oak",
        height=200.0,
        age_days=365,
        trunk_diameter="5.0cm",
    )

    oak.show()
    oak.produce_shade()
    print(f"Tree {oak._name} now produces a shade of {oak._height} long and {oak.trunk_diameter} wide.")

    print("\n=== Vegetable")
    tomato = Vegetable(
        name="tomato",
        height=5.0,
        age_days=10,
        harvest_season="April",
        nutritional_value=0,
    )

    tomato.show()
