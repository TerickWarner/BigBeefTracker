from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv2, teamgamelog, boxscoresummaryv2
import pandas
import csv
import time
import datetime


LAST_GAME_IDS = []
print(LAST_GAME_IDS)
now = datetime.date.today()
one_day_ago = now - datetime.timedelta(days=1)
YESTERDAY = one_day_ago.strftime("%A, %B %d, %Y").upper()
print(YESTERDAY)
#CREATE A CSV FILE WITH EACH TEAMS ID NUMBER IF NOT ALREADY DONE
# nba_teams = teams.get_teams()
# nba_teams_ids = pandas.DataFrame(nba_teams, columns=["id"])
# nba_teams_ids.to_csv('nba_teams_ids.csv', index=False)
# time.sleep(10)

#AS OF NOW THIS CODE WILL RUN AT 2:00 a.m. EST TO ENSURE WE GET EVERY FINISHED GAME
i = 0
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
            if (int(last_game.GAME_ID) not in LAST_GAME_IDS) and game_date == YESTERDAY:
                LAST_GAME_IDS.append(int(last_game.GAME_ID))
                for (key, value) in player_stats["REB"].items():
                    try:
                        if value >= 10:
                            print(f"{player_stats['PLAYER_NAME'][key]} ({player_stats['TEAM_ABBREVIATION'][key]}) had {int(value)} rebounds on {game_date} ")
                            print("Thats a lot of ROAST BEEF (which is rebounds)")
                            i+=1
                        else:
                            pass
                    except TypeError:
                        pass
            else:
                pass
            time.sleep(1)

if i == 0:
    print(f'No big beefs on {YESTERDAY.title()}')
