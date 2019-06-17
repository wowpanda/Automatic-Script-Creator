import shutil
import os
import json

with open('config.json', 'r') as config_file:
    data=config_file.read()
config = json.loads(data)

scriptName = input('>>> Name of the script: ')
scriptName = config["script_prefix"] + scriptName
dest = config["script_location"] + scriptName

if os.path.exists(config["script_location"]):
    if not os.path.exists(dest):
        shutil.copytree("boilerplate", dest)
        print("[Success]: Created script [" + scriptName + "]")
else:
    print("[Error]: Script location does not exist!")

input("Press Enter to exit")