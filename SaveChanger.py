# Created by earllgray aka Nick Furlo 1/19/2020
import os, sys, getopt, shutil
from datetime import datetime


def main():
    # Parse arguments
    args(sys.argv[1:])


def overwrite():
    # delete old file
    try:
        os.remove(save_path)
        print("Old save was deleted.")
    except Exception as e:
        print(e)
        print("Could Not Remove File.")
    # copy new save file
    try:
        shutil.copyfile('AllWorlds.sav', save_path)
        print("Save file coppied successfully")
    except Exception as e:
        print(e)
        print("Could not copy save file.")
        sys.exit(2)

# Backup current save file
def backup():
    try:
        working_dir = os.getcwd()
        save_name = 'user_param-' + (str(datetime.now().strftime("%m-%d-%Y_%I.%M.%S"))) + '.sav'
        backup_path = os.path.join(working_dir, save_name)
        print('tmp: ' + backup_path)
        shutil.copy2(str(save_path), str(save_name))
        print("Backup was successfully coppied to "+ str(backup_path))
    except Exception as e:
        print(e)
        print("BACKUP FAILED")
        sys.exit(2)

def args(argv):
    try:
        opts, args = getopt.getopt(argv, "hb", '')
    except getopt.GetoptError:
        print
        "Run 'python SaveChanger.py -h' for usage"
        sys.exit(2)
    if len(argv) == 0:
        overwrite()
    for opt, arg in opts:
        # print("opt: " + opt + "\nagr: " + arg)
        if opt == '-h':
            print(
                "Overwrite Current Save file: 'python SaveChanger.py' \nBackup current save file to script directory: 'python SaveChanger.py -b'")
            sys.exit()
        elif opt == "-b":
            backup()


# Get path for save file
appdata_path = os.getenv('APPDATA')
save_path = os.path.join(appdata_path, r"Sega\SuperMonkeyBallBananaBlitzHD\SAVE\user_param.sav")

main()
