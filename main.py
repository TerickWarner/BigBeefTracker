from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv2, teamgamelog, boxscoresummaryv2
import pandas
import csv
import time
from datetime import datetime


LAST_GAME_IDS = []
print(LAST_GAME_IDS)
# STEP 1: CREATE A CSV FILE WITH EACH TEAMS ID NUMBER
# nba_teams = teams.get_teams()
# nba_teams_ids = pandas.DataFrame(nba_teams, columns=["id"])
# nba_teams_ids.to_csv('nba_teams_ids.csv', index=False)
# time.sleep(10)

#STEP 2: FIND THE LAST GAME PLAYED BY EACH TEAM
# time.sleep(2)
# gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612743)
# time.sleep(2)
# game = gamefinder.get_data_frames()[0]
# last_game = game.head(1)

#STEP 3: USE GAME_ID TO FIND DATE
# time.sleep(2)
# box_score = boxscoresummaryv2.BoxScoreSummaryV2(game_id=last_game.GAME_ID)
# game_date = str(box_score.game_info.get_data_frame()['GAME_DATE'][0])

#STEP 4: GET THE CURRENT DAY IN WEEKDAY, MONTH DAY, YEAR FORMAT
now = datetime.now()
d2 = now.strftime("%A, %B %d, %Y")
print(d2.upper())

#STEP 5: LOOP THROUGH THE CSV FILE TO GET TEAM IDS
with open('nba_teams_ids.csv', newline='') as ids:
    reader = csv.reader(ids)
    for row in reader:
        if row == ['id']:
            pass
        else:
            gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=row)
            game = gamefinder.get_data_frames()[0]
            last_game = game.head(1)

            time.sleep(1)
            box_score_summary = boxscoresummaryv2.BoxScoreSummaryV2(game_id=last_game.GAME_ID)
            game_date = str(box_score_summary.game_info.get_data_frame()['GAME_DATE'][0])
            box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=last_game.GAME_ID)
            player_stats = box_score.player_stats.get_data_frame()
            if (int(last_game.GAME_ID) not in LAST_GAME_IDS):
                LAST_GAME_IDS.append(int(last_game.GAME_ID))
                for (key, value) in player_stats["REB"].items():
                    if value > 10:
                        print(f"{player_stats['PLAYER_NAME'][key]} had {int(value)} rebounds ")
                print(LAST_GAME_IDS)
            else:
                print("Game already used")
            time.sleep(1)

#STEP 6: NOW IF A GAME HAS BEEN USED DON'T USE THAT MATCH UP AGAIN
#Could we add each game id to a csv that changes and use a simple if x in game_id csv pass


# player_stats = box_score.player_stats.get_data_frame()
# print(player_stats)
