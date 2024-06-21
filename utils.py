import os
import json
from service import GAMES_REPO_PATH, EMULATORS_REPO_PATH

def validate_dir_stuct():
    checkList = [GAMES_REPO_PATH, EMULATORS_REPO_PATH]

    for dir in checkList:
        if not os.path.isdir(dir):
            os.makedirs(dir)

def collect_all_titles():
    collected_titles = list()
    for game in os.listdir("games"):
        with open("games\\" + game + '\\info.json') as f:
            d = json.load(f)
            collected_titles.append(
                {
                    "title": d["about"]["title"],
                    "id" : game
                }
            )

    return collected_titles

def collect_all_emulators_titles():
    collected_titles = list()
    for emulator in os.listdir("emulators"):
        with open("emulators\\" + emulator + '\\info.json') as f:
            d = json.load(f)
            collected_titles.append(
                {
                    "title": d["about"]["title"],
                    "path" : emulator
                }
            )

    return collected_titles
