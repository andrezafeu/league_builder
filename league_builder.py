import csv
import random


if __name__ == "__main__":

    TEAMS = ['Sharks', 'Dragons', 'Raptors']
    players_with_experience = []
    players_without_experience = []


    def build_players_lists():
        with open('soccer_players.csv', newline = '') as csvfile:
            soccer_players = csv.DictReader(csvfile)
            for row in soccer_players:
                del row['Height (inches)']
                if row['Soccer Experience'] == 'YES':
                    players_with_experience.append(row)
                else:
                    players_without_experience.append(row)


    def build_letter(team, player, game_datetime):
        player_names = player['Name'].lower().split()
        file_name = "_".join(player_names) + ".txt"
        message = "Dear {},\n\n{} will be playing for the {} and the first practice will be on {}."
        with open(file_name, 'w') as letterfile:
            letterfile.write(message.format(player['Guardian Name(s)'], player['Name'], team, game_datetime))


    def get_random_players(players_list, number_of_players):
        return random.sample(players_list, int(number_of_players/len(TEAMS))) 


    def add_players(team, players_list, number_of_players):
        sample = get_random_players(players_list, number_of_players)
        fieldnames = ['Name', 'Soccer Experience', 'Guardian Name(s)']
        for player in sample:
            players_list.remove(player)
            teamwriter = csv.DictWriter(teamfile, fieldnames=fieldnames)
            teamwriter.writerow(player)
            build_letter(team, player, game_datetime)


    def build_teams():
        number_of_players_with_experience = len(players_with_experience)
        number_of_players_without_experience = len(players_without_experience)
        for team in TEAMS:
            teamfile.write(team + "\n")
            add_players(team, players_with_experience, number_of_players_with_experience)
            add_players(team, players_without_experience, number_of_players_without_experience)


    # allows the same script to be used on different leagues/tournaments
    game_datetime = input("What's the date and time of the game? ")


    build_players_lists()


    with open('teams.txt', 'a') as teamfile:
        build_teams()
        print("Teams sucessfully created!")