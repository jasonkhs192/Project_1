from tkinter import *
from riotwatcher import LolWatcher, ApiError
from datetime import datetime

def test(api_key, name, match_num):
    try:
        lol_watcher = LolWatcher(api_key)
        my_region = 'na1'
        me = lol_watcher.summoner.by_name(my_region, name)
        accountID = me["accountId"]
        mlst = lol_watcher.match.matchlist_by_account(my_region, accountID)
        recent_match = mlst["matches"][int(match_num)]["gameId"]

        my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])

        
        print("Hello, {}. Welcome to Summoner's Rift!".format(me["name"]))

        stat_count = 0
        for count in my_ranked_stats:
            stat_count = stat_count + 1
        if stat_count == 1:
            stat1 = my_ranked_stats[0]
            print("Rank: {} {} {} LP".format(stat1["tier"], stat1["rank"], stat1["leaguePoints"]))

        if stat_count == 2:
            stat1 = my_ranked_stats[0]
            stat2 = my_ranked_stats[1]
            if stat1["queueType"] == "RANKED_SOLO_5x5":
                print("Rank: {} {} {} LP".format(stat1["tier"], stat1["rank"], stat1["leaguePoints"]))
            else:
                print("Rank: {} {} {} LP".format(stat2["tier"], stat2["rank"], stat2["leaguePoints"]))

        game = lol_watcher.match.by_id(my_region, recent_match)

        print("---------------------------------------------")
        print("             Last Match Status")
        print("---------------------------------------------")

        if game["queueId"] == 420:
            print("Game Type: Ranked")
        else:
            print("Game Type: Casual")

        if game["gameType"] == "CUSTOM_GAME":
            print("**Custom Game**")

        classic = 0
        if game["gameMode"] == "CLASSIC":
            classic = classic + 1
            print("Map: Summoner's Rift")
        elif game["gameMode"] == "ARAM":
            print("Map: Howling Abyss [ARAM]")
        elif game["gameMode"] == "URF":
            print("Map: Summoner's Rift [URF]")
        elif game["gameMode"] == "ONEFORALL":
            print("Map: Summoner's Rift [OneForAll]")
        else:
            print("Map: Unknown")

        # find participant id with account id
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        position = 0
        for x in lst:
            if game["participantIdentities"][x]["player"]["accountId"] == accountID:
                position = position + x
                if game["participants"][x]["stats"]["win"]:
                    print("-Match Status: Victory")
                else:
                    print("-Match Status: Defeat")

        duration_seconds = game["gameDuration"]
        duration_minutes = duration_seconds // 60
        duration_seconds_remainder = duration_seconds % 60
        if duration_seconds_remainder < 10:
            duration_seconds_remainder = "0" + str(duration_seconds_remainder)

        print("-Game Length: {}:{}".format(duration_minutes, duration_seconds_remainder))

        timestamp = game["gameCreation"] / 1000
        matchdate_start = round(timestamp)
        dt_object = datetime.fromtimestamp(matchdate_start)
        utc_format = dt_object
        utc = datetime.strptime(str(utc_format), '%Y-%m-%d %H:%M:%S')
        time = utc.strftime("%Y-%m-%d %I:%M:%S %p")
        print("-Match Start Date & Time: {}".format(time))

        matchdate_end = matchdate_start + duration_seconds
        dt_object = datetime.fromtimestamp(matchdate_end)
        utc_format = dt_object
        utc = datetime.strptime(str(utc_format), '%Y-%m-%d %H:%M:%S')
        time = utc.strftime("%Y-%m-%d %I:%M:%S %p")
        print("-Match End Date & Time: {}".format(time))

        time_diff = (datetime.now().timestamp() - matchdate_end)
        if time_diff // 60 < 60:
            time_diff_min = time_diff // 60
            time_diff_sec = round(time_diff % 60)
            if time_diff_sec == 0:
                time_diff_sec = "00"
            elif time_diff_sec < 10:
                time_diff_sec = "0" + str(time_diff_sec)
            print("-Match Ended {}min {}sec ago".format(int(time_diff_min), time_diff_sec))
        else:
            time_diff_min = time_diff / 60
            time_diff_hour = time_diff_min / 60
            print("-Match Ended {} hour(s) ago.".format(round(time_diff_hour)))

        champion_list = lol_watcher.data_dragon.champions("10.22.1")
        # print(test["data"]["Aatrox"]["key"])

        my_champion_id = (game["participants"][position]["championId"])

        for champion in champion_list["data"]:
            if (champion_list["data"][champion]["key"]) == str(my_champion_id):
                print("-Champion: {}".format(champion))

        kills = game["participants"][position]["stats"]["kills"]
        deaths = game["participants"][position]["stats"]["deaths"]
        assists = game["participants"][position]["stats"]["assists"]
        survive_time = game["participants"][position]["stats"]["longestTimeSpentLiving"]
        kda = (kills + assists) / deaths
        kda = round(kda, 2)

        print("-KDA: {}/{}/{} | Ratio: {}:1".format(kills, deaths, assists, kda))
        survive_time_minutes = survive_time // 60
        survive_remainder = survive_time % 60
        if survive_remainder < 10:
            survive_remainder = "0" + str(survive_remainder)
        print(
            "-Longest time spent living: {} seconds. [{}:{}]".format(survive_time, survive_time_minutes,
                                                                     survive_remainder))

        if classic == 1:
            wardsPlaced = game["participants"][position]["stats"]["wardsPlaced"]
            wardsKilled = game["participants"][position]["stats"]["wardsKilled"]
            visionWardsBoughtInGame = game["participants"][position]["stats"]["visionWardsBoughtInGame"]
            visionScore = game["participants"][position]["stats"]["visionScore"]

            print("-Wards Placed Count: {}".format(wardsPlaced))
            print("-Wards Killed Count: {}".format(wardsKilled))
            print("-Pink Wards Bought Count: {}".format(visionWardsBoughtInGame))
            time = duration_seconds / 60
            above_average = time * 1.5
            average = time
            if visionScore > above_average:
                print("-Vision Score: {} | Above Average".format(visionScore))
            elif visionScore <= above_average and visionScore >= average:
                print("-Vision Score: {} | Average".format(visionScore))
            elif visionScore < average:
                print("-Vision Score: {} | Below Average".format(visionScore))
    except ApiError as err:
        if err.response.status_code == 403:
            print("Wrong API Key")
        else:
            print("something")


def submit():
    api_key = api_entry.get()
    name = id_entry.get()
    match_num = match_count_entry.get()
    test(api_key, name, match_num)



def clear():
    pass

root = Tk()
root.title("Jason.GG")
root.resizable(False, False)

api_frame = LabelFrame(root)
api_frame.pack(fill="x")

api_label = Label(api_frame, text="API Key: ")
api_label.pack(side="left")

api_entry = Entry(api_frame)
api_entry.pack(side="right")

id_frame = LabelFrame(root)
id_frame.pack(fill="x")

id_label = Label(id_frame, text="Summoner's Name: ")
id_label.pack(side="left")

id_entry = Entry(id_frame)
id_entry.pack(side="right")

match_count_frame = LabelFrame(root)
match_count_frame.pack(fill="x")

match_count_label = Label(match_count_frame, text="Past Match #: ")
match_count_label.pack(side="left")

match_count_entry = Entry(match_count_frame)
match_count_entry.pack(side="right")

submit_button_frame = LabelFrame(root)
submit_button_frame.pack(fill="x")

clear_button_button = Button(submit_button_frame, text="Clear", command=clear)
clear_button_button.pack(side="right")

submit_button_button = Button(submit_button_frame, text="Submit", command=submit)
submit_button_button.pack(side="right")

root.mainloop()