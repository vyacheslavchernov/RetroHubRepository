# service.py
GAMES_REPO_PATH = "games\\"
EMULATORS_REPO_PATH = "emulators\\"

from utils import *
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

### /games/* routes ###

@app.route('/games/info/<title>', methods = ['GET'])
def get_game_info(title):
    return send_from_directory(directory = GAMES_REPO_PATH + title, path="info.json")

@app.route('/games/cover/<title>', methods = ['GET'])
def get_game_cover(title):
    return send_from_directory(directory = GAMES_REPO_PATH + title, path="cover.png")

@app.route('/games/rom/<title>/<rom>', methods = ['GET'])
def get_game_rom(title, rom):
    return send_from_directory(directory = GAMES_REPO_PATH + title, path=rom)

@app.route('/games/get_all_titles', methods = ['GET'])
def get_all_titles():
    return jsonify(collect_all_titles())

### /games/* routes ###

### /emulators/* routes ###

@app.route('/emulators/get/<title>/<platform>/<version>', methods = ['GET'])
def get_emulator(title, platform, version):
    dirPath = EMULATORS_REPO_PATH + title+ '\\' + platform + '\\' + version
    return send_from_directory(
        directory=dirPath, 
        path= os.listdir(dirPath)[0] 
    )

@app.route('/emulators/get_all_titles', methods = ['GET'])
def get_all_emulators():
    return jsonify(collect_all_emulators_titles())

@app.route('/emulators/info/<title>', methods = ['GET'])
def get_emulator_info(title):
    return send_from_directory(directory = EMULATORS_REPO_PATH + title, path="info.json")

### /emulators/* routes ###

if __name__ == '__main__':
    validate_dir_stuct()
    app.run(debug=True)