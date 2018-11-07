from bank import Bank
from timelines import Timelines
import pprint
import json
from pathlib import Path
import sys
'''
This app polls Watchout for the timeline list and then
generates buttons within companions data file.
This file is here-
C:\\Users\\Name\AppData\Roaming\Companion\db

This script overwrites the db located in this script's directory.
You'll need to copy and replace it, or backup and replace the original.

'''
try:
	ipAddress = sys.argv[1]
	print('Running from command prompt:\n IP Address is ',ipAddress)
except:
	ipAddress = '127.0.0.1'
	print('Running as local host')

timelineObj = Timelines()
timelineList = timelineObj.get_aux_timelines(ipAddress)

jsonData = {}#json.loads(file.read())

newBank= Bank(timelineList) # bank.py

jsonData['deviceconfig'] = {} # this is blank
jsonData['bank'] = newBank.get_bank()['buttons'] #getting the list of buttons
jsonData['bank_actions']=newBank.get_bank()['actions'] #getting the list of bank actions
jsonData['userconfig']={} #this is blank.. Not sure what this is
jsonData['instance'] = {"B1M9CUzoX": {
                                    "instance_type": "watchout-production",
                                    "label": "watchout-production",
                                    "host": "{ipAddress}".format(ipAddress = ipAddress)}}

jsonData['userconfig'] = {'page_direction_flipped':True}

pprint.pprint(jsonData)
pathToDB = str(Path.home())+str(Path('\AppData\Roaming\Companion\db'))
#print(pathToDB)
writeFile = open(pathToDB,'w')

writeFile.write(json.dumps(jsonData,indent=12))
writeFile.close()
