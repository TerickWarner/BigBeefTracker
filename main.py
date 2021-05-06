from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder, boxscoretraditionalv2, boxscoresummaryv2
import time
import datetime

i = 0
BIG_BEEF_COUNTER = 0
LAST_GAME_IDS = []
teams = teams.get_teams()

def get_yesterday():
    now = datetime.date.today()
    one_day_ago = now - datetime.timedelta(days=1)
    yesterday = one_day_ago.strftime("%Y-%m-%d")
    return yesterday

def get_team_id(ident):
    return teams[ident]["id"], teams[ident]["full_name"]


def get_last_game():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=get_team_id(i))
    time.sleep(1)
    last_game_date = gamefinder.get_data_frames()[0]['GAME_DATE'][0]
    last_game_id = gamefinder.get_data_frames()[0]['GAME_ID'][0]
    return last_game_id, last_game_date


def get_player_reb_stats():
    box_score = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=get_last_game()[0])
    time.sleep(1)
    player_reb_stats = box_score.player_stats.get_data_frame()[["PLAYER_NAME", "REB", 'TEAM_ABBREVIATION']]
    return player_reb_stats


def get_game_status():
    end_game = boxscoresummaryv2.BoxScoreSummaryV2(game_id=get_last_game()[0])
    game_status = end_game.game_summary.get_data_frame()["GAME_STATUS_ID"][0]
    time.sleep(1)
    return game_status





#MAY HAVE TO CHECK IF REBOUNDS ARE NONE TO MAKE SURE STATS ARE THERE EVEN IF GAME STATUS == 3


while i < 30:
    if get_game_status() == 3 and (get_last_game()[0] not in LAST_GAME_IDS) and (get_yesterday() == get_last_game()[1]):
        LAST_GAME_IDS.append(get_last_game()[0])
        for (key, value) in get_player_reb_stats()["REB"].items():
            try:
                if value >= 20:
                    print(f"{get_player_reb_stats()['PLAYER_NAME'][key]} ({get_player_reb_stats()['TEAM_ABBREVIATION'][key]}) had {int(get_player_reb_stats()['REB'][key])} rebounds")
                    print("Thats a lot of ROAST BEEF (which is rebounds)")
                    BIG_BEEF_COUNTER += 1
                else:
                    pass
            except TypeError:
                break
    i += 1
    time.sleep(1)

if BIG_BEEF_COUNTER == 0:
    print(f"There were no BIG BEEFS on {get_yesterday()}")




