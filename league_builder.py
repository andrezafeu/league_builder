import csv
import random

TEAMS = ['Sharks', 'Dragons', 'Raptors']

def build_players_lists(players_with_experience, players_without_experience):
    with open('soccer_players.csv', newline = '') as csvfile:
        soccer_players = csv.DictReader(csvfile)
        for row in soccer_players:
            del row['Height (inches)']
            if row['Soccer Experience'] == 'YES':
                players_with_experience.append(row)
            else:
                players_without_experience.append(row)


# allows the same script to be used on different leagues/tournaments
def get_game_datetime():
    return input("What's the date and time of the game? ")


def build_letter(team, player, game_datetime):
    player_names = player['Name'].lower().split()
    file_name = "_".join(player_names) + ".txt"
    message = "Dear {},\n\n{} will be playing for the {} and the first practice will be on {}."
    with open(file_name, 'w') as letterfile:
        letterfile.write(message.format(player['Guardian Name(s)'], player['Name'], team, game_datetime))


def get_random_players(players_list, number_of_players):
    return random.sample(players_list, int(number_of_players/len(TEAMS))) 


def add_players(team, teamfile, players_list, number_of_players):
    sample = get_random_players(players_list, number_of_players)
    fieldnames = ['Name', 'Soccer Experience', 'Guardian Name(s)']
    for player in sample:
        players_list.remove(player)
        teamwriter = csv.DictWriter(teamfile, fieldnames=fieldnames)
        teamwriter.writerow(player)
        build_letter(team, player, game_datetime)


def build_team_file():
    with open('teams.txt', 'w') as teamfile:
        number_of_players_with_experience = len(players_with_experience)
        number_of_players_without_experience = len(players_without_experience)
        for team in TEAMS:
            teamfile.write(team + "\n")
            add_players(team, teamfile, players_with_experience, number_of_players_with_experience)
            add_players(team, teamfile, players_without_experience, number_of_players_without_experience)
        print("Teams sucessfully created!")


if __name__ == "__main__":

    players_with_experience = []
    players_without_experience = []

    game_datetime = get_game_datetime()

    build_players_lists(players_with_experience, players_without_experience)

    build_team_file()