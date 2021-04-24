from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv2
import pandas
import csv



#This gets all the teams put in a dictionary
nba_teams = teams.get_teams()
#need to get team ids to a csv
nba_teams_ids = pandas.DataFrame(nba_teams, columns=["id"])
nba_teams_ids.to_csv('nba_teams_ids.csv', index=False)

#now we need to loop through csv to get last game played
#NOW NEED TO FIGURE OUT HOW TO GET THE LAST GAME PLAYED
for value in nba_teams_ids['id']:
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=value)
    games = gamefinder.get_data_frames()[-1]
    games.head()


















# # for one team we are able to get their ID in order to find their game logs
# pacers = [team for team in nba_teams if team['abbreviation'] == 'IND'][0]
# pacers_id = pacers['id']
#
#
# #once we have the idea we use endpoint leaguegamefinder to get dataframe of entire history of games
# gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=pacers_id)
# games = gamefinder.get_data_frames()[0]
# games.head()
#
# #we need to eventually get the last game of the team played so we can track if there are any big beefs
# #We use the sort_values method and get the ending with iloc. FIGURE OUT HOW AND WHY THIS WORKS
# last_cers_game = games.sort_values('GAME_DATE').iloc[-1]
#
#
# #We get the game ID for the last game the Pacers played. Being able to get the game id from the last game played will
# #come in handy when we want to get the game id of all games played that night. The .GAME_ID method will return any
# #game id for a game, just have to make sure it is on the right day.
# print(last_cers_game.GAME_ID)
#
# #we now have a boxscore for the last game the pacers played
# box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id='0022000882')
# player_stats = box_score.player_stats.get_data_frame()
#
# #prints out the number of rebounds player at index 1 had, need to iterate through
# # print(int(player_stats["REB"][1]))
#
#
# for (key, value) in player_stats["REB"].items():
#     if value > 10:
#         print(f"{player_stats['PLAYER_NAME'][key]} had {int(value)} rebounds ")
#
#
# # for key in player_stats["REB"]:
# #     if key > 10:
# #         print(key)
#
#
#
#
#
#
# # player_dict = players.get_players()
# #
# # active_dict = players.get_active_players()
# # print(active_dict)
# # #
# # for key in active_dict:
# #     print(key['full_name'])


