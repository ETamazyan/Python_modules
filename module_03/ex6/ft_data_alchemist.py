
#!/usr/bin/env python3

import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    # Original list of players
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]

    print("Initial list of players:", players)

    capitalized_players = [player.capitalize() for player in players]

    print("New list with all names capitalized:", capitalized_players)

    capitalized_only = [
        player for player in players if player[0].isupper()
    ]

    print("New list of capitalized names only:", capitalized_only)

    score_dict = {
        player: random.randint(0, 1000)
        for player in capitalized_players
    }

    print("Score dict:", score_dict)

    average = round(
        sum(score_dict.values()) / len(score_dict), 2
    )

    print(f"Score average is {average}")

    high_scores = {
        player: score
        for player, score in score_dict.items()
        if score > average
    }

    print("High scores:", high_scores)
