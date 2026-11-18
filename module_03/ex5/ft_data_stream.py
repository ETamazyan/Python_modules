#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]

    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "swim",
        "climb",
        "use",
        "release"
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events[index]

        del events[index]

        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        player, action = next(event_generator)
        print(f"Event {i}: Player {player} did action {action}")

    list_generator = gen_event()

    event_list = [next(list_generator) for _ in range(10)]

    print("Built list of 10 events:", event_list)

    for event in consume_event(event_list):
        print("Got event from list:", event)
        print("Remains in list:", event_list)
