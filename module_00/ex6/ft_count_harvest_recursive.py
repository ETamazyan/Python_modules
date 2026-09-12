count = 1

def ft_count_harvest_recursive(count):
    if count > 5:
        print("Harvest time!")
        return
    print(f"Day {count}")
    ft_count_harvest_recursive(count + 1)


if __name__ == "__main__":
    ft_count_harvest_recursive(count)
    
