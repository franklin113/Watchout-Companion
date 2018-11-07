from bank import Bank
from timelines import Timelines
import pprint
import json
import sys


try:
	ipAddress = sys.argv[1]
	print('Running from command prompt:\n IP Address is ',ipAddress)
except:
	ipAddress = '127.0.0.1'
	print('Running as local host')

jsonData = {}#json.loads(file.read())

timelineObj = Timelines()
timelineList = timelineObj.connection(ipAddress)

newBank= Bank(timelineList)


jsonData['deviceconfig'] = {} # this is blank
jsonData['bank'] = newBank.get_bank()['buttons'] #getting the list of buttons
jsonData['bank_actions']=newBank.get_bank()['actions'] #getting the list of bank actions
jsonData['userconfig']={} #this is blank.. Not sure what this is
jsonData['instance'] = {"B1M9CUzoX": {
                                    "instance_type": "watchout-production",
                                    "label": "watchout-production",
                                    "host": "{ipAddress}"
                        }}
jsonData['userconfig'] = {'page_direction_flipped':True}


pprint.pprint(jsonData)


writeFile = open('db','w')

writeFile.write(json.dumps(jsonData,indent=12))
writeFile.close()
