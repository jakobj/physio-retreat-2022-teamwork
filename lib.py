import numpy as np


def load_names():
    names = []
    with open("./names.txt", "r") as f:
        for l in f:
            names.append(l.replace("\n", ""))
    return names


def create_teams(*, team_sizes):
    names = load_names()
    N = len(names)
    rng = np.random.default_rng()
    i = 0
    n = 0
    while n < N:
        team_size = team_sizes[i % len(team_sizes)]
        team = create_team(names, team_size, rng)
        if team:
            print(team)
            n += team_size
        i += 1
    assert len(names) == 0


def create_team(names, team_size, rng):
    if team_size > len(names):
        return []
    team = []
    for _ in range(team_size):
        rng.shuffle(names)
        team.append(names.pop())
    return team


def generate_random_numbers(*, n):
    rng = np.random.default_rng()
    return rng.integers(1, 100, size=n).tolist()
