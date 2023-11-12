from player_reader import PlayerReader
from statistics_service import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    nationality = "FIN"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    print(f"Players from {nationality}:\n")
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
