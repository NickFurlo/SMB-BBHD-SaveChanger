# SMB-BBHD-SaveChanger
Super Monkey Ball: Banana Blitz HD SaveChanger

	This script will allow you to setup save files for All Worlds speedruns of BBHD. It can overwrite your 
	save file with a new one and backup your current save file. 

Getting Started

  	If you have not already done so, install python (https://www.python.org/downloads/)
  
	Before running the script you must disable Steam Cloud synchronization for BBHD. You can do this by
	right clicking on the game in your steam library, clicking preferences, clicking on the "UPDATES" tab
	and then unchecking the box at the bottom   that says "Enable Steam Cloud synchronization for Super 
	Monkey Ball: Banana Blitz HD". 
	
	I have included the save file I use for All Worlds speedruns. All of the worlds have been reset, sonic
	is unlocked, and I have all options the way I like them.

Usage

    This script has two fucntions, backing up and restoring save files.
    
    BACKUP
    
      Run "Python SaveChanger.py -b" to copy your current save file to the folder the script is in. 
   
      When you backup a save for use with All Worlds speedruns you will want to make sure you have entered 
      every world, paused, and clicked "Restart World". You will also want to make sure that all of the 
      options (sound, graphics, controls, etc) are the way you like them. 
    
    RESTORING
    
      The first step is to close BBHD. You can do this quickly by going to steam and clicking the green 
      "STOP" button.
      Then run "Python SaveChanger.py" to restore your save file. 
      The save file you want to restore must be named "AllWorlds.sav" and be in the same folder as SaveChanger.py.

Prerequisites

	Python 3.6+ (https://www.python.org/downloads/)

Version

	Version 1.0

Authors

	earllgray aka Nick Furlo

License

	The GNU General Public License v3.0
