
# About RetroHub Repository
RetroHub is repository for use with [RetroHub Desktop client](https://github.com/vyacheslavchernov/RetroHubDesktop). Provide access to information, ROMs, and emulators that repository stores.
Reposity by it self **don't contain any game or emulator**. Make sure that you use RetroHub in an appropriate way.

# # RetroHub Repository API
	# Games relative
	['GET'] /games/info/<title> - get info.json for an game
	['GET'] /games/cover/<title> - get cover art for an game
	['GET'] /games/rom/<title>/<rom> - get specific ROM for an game (<rom> can be extracted from info.json of game)
	['GET'] /games/get_all_titles - get list of all stored titles
	
	# Emulators relative
	['GET'] /emulators/info/<title> - get info.json for an emulator
	['GET'] /emulators/get/<title>/<platform>/<version> - get an emulator of specific version for specific platform (information about see in info.json for emulator)
	['GET'] /emulators/get_all_titles - get list of all stored emulators
	

# How to run

>1. Install dependecies from requirements.txt

>2. Run service.py

# Repository structure

>* games/ directory contain all available games, emulators/ directory contain all available emulators

>* Any game directory in games/ should have unique name

>* Any emulator directory in emulators/ should have unique name

  

# Example of an game directory structure

 - **games**
	 - **title** 
		 - **cover.png**
		 - **info.json**
		 - **game-rom.gen**

> **games** - games root directory
> **title**  - unique game name
> **cover.png** - cover art for game. Only .PNG for now
> **info.json** - information about game
> **game-rom.gen** - game ROM, can be more than one for the game

# Example of info.json for an game

        {
    
			    "about" : {    
				    "title": "game title",    
				    "released" : 1998,    
				    "cover": "/cover.jpg",    
				    "platform": "Sega Genesis/Mega Drive",    
				    "rating": "10/10",    
				    "developer": "Dev",
				    "players": "1",
				    "description": "som decription"
		    }, 
		    "roms" : [
			    {    
				    "official" : true,    
				    "region" : "Japan",    
				    "title" : "Game Title",    
				    "path" : "gameTitle.gen"    
			    }    
		   ]  
	    }

# Example of an emulator directory structure
- **emulators**
	- **emulator title**
		- **info.json**
		- **platform**
			- **version**
				- **emulator.zip**
			- **version**
				- **emulator.zip**
		- **platform**
			- **version**
				- **emulator.zip**
> **emulators** - root directory for emulators
> **emulator title** - title of an emulator, shold be unique
> **info.json** - information about emulator
> **platform** - folder for specific platform emulator distributives (like win32, debian, etc)
> **version** - version of emulator distributive
> **emulator.zip** - emulator distributive, shold be archived in zip

# Example of info.json for an emulator

    {
	    "about": {
		    "title": "BlastEm",
		    "emulatingPlatform": "Sega Genesis/Mega Drive",
		    "description": "",
		    "creatorUrl": "https://www.retrodev.com/blastem/"
	    },
	    "distributives": [
		    {
			    "platform": "win32",
			    "version": "0.6.2",
			    "distroName": "/blastem-win32-0.6.2.zip"
		    }
	    ]
    }

