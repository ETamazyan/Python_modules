class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self):
        self.height += 0.8

    def age(self):
        self.age_days += 1


plant = Plant("Rose", 25.0, 30)

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    print(f"{plant.name}: {plant.height:.1f}cm, {plant.age_days} days old")

    initial_height = plant.height

    for day in range(1, 8):
        plant.grow()
        plant.age()
        print(f"=== Day {day} ===")
        print(f"{plant.name}: {plant.height:.1f}cm, {plant.age_days} days old")

    print(f"Growth this week: {round(plant.height - initial_height, 1)}cm")
