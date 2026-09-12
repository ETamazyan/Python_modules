
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")


if __name__ == "__main__":
    ft_seed_inventory("tomato", 15, "packets")
    ft_seed_inventory("carrot", 8, "grams")
    ft_seed_inventory("lettuce", 12, "area")
