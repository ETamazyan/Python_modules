# class Class:
#     pass

class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days


p1 = Plant("Rose", 25, 30)
p2 = Plant("Sunflower", 80, 45)
p3 = Plant("Cactus", 15, 120)


if __name__ == "__main__":
    print(f"{p1.name}: {p1.height}cm, {p1.age_days} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.age_days} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.age_days} days old")
