class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age_days
        self._stats = Plant.Statistics()

    def grow(self) -> None:
        self._height += 0.8
        self._stats.record_grow()

    def age(self) -> None:
        self._age_days += 1
        self._stats.record_age()

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")
        self._stats.record_show()

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

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0, 0)

    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )


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
        self._has_bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        number_of_seeds: int,
    ) -> None:
        super().__init__(name, height, age_days, color)
        self.number_of_seeds = number_of_seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.number_of_seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.number_of_seeds = 42


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age_days: int,
        trunk_diameter: int,
    ) -> None:
        super().__init__(name=name, height=height, age_days=age_days)
        self._stats = Tree.TreeStatistics()
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        self._stats.record_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")

    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")


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
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("=== Flower")

    rose = Flower("Rose", 15, 10, "red")

    rose.show()
    display_statistics(rose)

    rose.grow()
    rose.bloom()

    rose.show()
    display_statistics(rose)

    print("=== Tree")

    oak = Tree("Oak", 200, 365, 5)

    oak.show()
    display_statistics(oak)

    oak.produce_shade()

    display_statistics(oak)

    print("=== Seed")

    sunflower = Seed("Sunflower", 80, 45, "yellow", 0)

    sunflower.show()

    sunflower.grow()
    sunflower.age()
    sunflower.bloom()

    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")

    anonymous = Plant.create_anonymous()

    anonymous.show()
    display_statistics(anonymous)
