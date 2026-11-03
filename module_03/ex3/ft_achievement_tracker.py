#!/usr/bin/env python3
import random

achievements = [
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Collector Supreme",
    "World Savior",
    "Speed Runner",
    "Strategist",
    "Survivor",
    "Treasure Hunter",
    "Unstoppable",
    "Untouchable",
    "Sharp Mind",
    "Hidden Path Finder"
]


def gen_player_achievements() -> set:
    number = random.randint(3, 5)

    selected = set(random.sample(achievements, number))
    return selected.union({"Untouchable"})


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print("")

    all_unlocked = alice.union(bob, charlie, dylan)
    print("All distinct achievements:", all_unlocked)
    print("")

    common = alice.intersection(bob, charlie, dylan)
    print("Common achievements:", common)
    print("")

    alice_only = alice.difference(bob.union(charlie, dylan))
    bob_only = bob.difference(alice.union(charlie, dylan))
    charlie_only = charlie.difference(alice.union(bob, dylan))
    dylan_only = dylan.difference(alice.union(bob, charlie))

    print("Only Alice has:", alice_only)
    print("Only Bob has:", bob_only)
    print("Only Charlie has:", charlie_only)
    print("Only Dylan has:", dylan_only)
    print("")

    achievement_universe = set(achievements).union({"Untouchable"})

    print("Alice is missing:", achievement_universe.difference(alice))
    print("Bob is missing:", achievement_universe.difference(bob))
    print("Charlie is missing:", achievement_universe.difference(charlie))
    print("Dylan is missing:", achievement_universe.difference(dylan))
