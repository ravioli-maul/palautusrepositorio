import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(player_dict)
            players.append(player)

    players.sort(key=lambda player: player.totals, reverse=True)

    print("Players from FIN:\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
