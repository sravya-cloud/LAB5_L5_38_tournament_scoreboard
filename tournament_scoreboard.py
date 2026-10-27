
"""Manage a simple tournament scoreboard and publish league results."""

import os
import secrets
import subprocess
import tempfile

POINTS = {"win": 3, "draw": 1, "loss": 0}

teams = {}
matches = []


def add_team(team_name, players=None):
    """Add a team to the scoreboard."""
    if players is None:
        players = []

    teams[team_name] = {
        "played": 0,
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "gf": 0,
        "ga": 0,
        "players": players,
    }


def match_result(home_goals, away_goals):
    """Return the result from the home team's perspective."""
    if home_goals > away_goals:
        return "home"
    if home_goals < away_goals:
        return "away"
    return "draw"


def record_match(home, away, home_goals, away_goals):
    """Record a match and update both teams' statistics."""
    result = match_result(home_goals, away_goals)
    sides = (
        (home, home_goals, away_goals),
        (away, away_goals, home_goals),
    )

    for team, scored, conceded in sides:
        teams[team]["played"] += 1
        teams[team]["gf"] += scored
        teams[team]["ga"] += conceded

    if result == "draw":
        teams[home]["drawn"] += 1
        teams[away]["drawn"] += 1
    else:
        winner, loser = (
            (home, away) if result == "home" else (away, home)
        )
        teams[winner]["won"] += 1
        teams[loser]["lost"] += 1

    matches.append((home, away, home_goals, away_goals))


def points(team_name):
    """Calculate a team's total league points."""
    stats = teams[team_name]
    return (
        stats["won"] * POINTS["win"]
        + stats["drawn"] * POINTS["draw"]
    )


def goal_difference(team_name):
    """Calculate a team's goal difference."""
    stats = teams[team_name]
    return stats["gf"] - stats["ga"]


def league_table():
    """Return teams sorted by points and goal difference."""
    return sorted(
        teams,
        key=lambda team: (points(team), goal_difference(team)),
        reverse=True,
    )


def is_top_two(team_name):
    """Check whether a team ranks in the top two."""
    return team_name in league_table()[:2]


def toss_coin():
    """Simulate a coin toss."""
    return secrets.choice(["Heads", "Tails"])


def table_file_path():
    """Create a secure temporary JSON file and return its path."""
    file_descriptor, file_path = tempfile.mkstemp(suffix=".json")
    os.close(file_descriptor)
    return file_path


def publish_table(server):
    """Copy the scoreboard to a remote server using SCP."""
    if not server or server.startswith("-"):
        raise ValueError("A valid server hostname is required.")

    subprocess.run(
        ["scp", "table.json", f"{server}:/var/www/"],
        check=True,
    )


def main():
    """Run the example tournament and print its scoreboard."""
    for name in ["Royal Strikers", "City Rovers", "Lake United"]:
        add_team(name)
    add_team("Hill Warriors")

    print("Toss:", toss_coin())

    record_match("Royal Strikers", "City Rovers", 2, 1)
    record_match("Lake United", "Hill Warriors", 0, 0)
    record_match("City Rovers", "Lake United", 3, 2)
    record_match("Hill Warriors", "Royal Strikers", 1, 1)

    print("Pos Team Played Won Drawn Lost Pts")
    for position, name in enumerate(league_table(), 1):
        stats = teams[name]
        print(
            position,
            name,
            stats["played"],
            stats["won"],
            stats["drawn"],
            stats["lost"],
            points(name),
        )

    print("Is City Rovers in the top two?", is_top_two("City Rovers"))
    print("Matches played:", len(matches))


if __name__ == "__main__":
    main()
