import socket
#import pprint
import json

class json_parser():
	'''
	I copied this from one of my other programs so there may be some unnecessary stuff.
	It just parses the retrieved data, but it was meant to do more than just timeline info.
	'''
	def __init__(self):

		self.splitMessage = '' #this will hold the messages once split up
		self.jsonObj = '' #this will contain all the decoded json data

		pass

	def print_json(self, message):
		'''
		takes a message.. checks if it's actually multiple

		'''
		message = message
		print('Printing json string')
		print(json.dumps(message,indent=4))

	def split_messages(self,message):
		'''
		checks if the tcp commands actually repeated it's message
		returns a list of strings  -- NOT json objects
		but also changes the split message member
		'''
		# splits at 'Reply '


		try:
			self.splitMessage = message.split('Reply ')
			self.splitMessage.pop(0)
			print("PASSED: split message")
		except:
			print("Error splitting json message")

		return self.splitMessage

	def decode(self,message):
		'''
		this decodes the message and returns a json object
		also changes the jsonObj member
		'''
		try:
			if type(message) == list:

				self.jsonObj = []
				for i in message:
					self.jsonObj.append(json.loads(i))
				print("PASSED: decoded json list")

			elif type(message) == str:
				self.jsonObj=json.loads(message)
				print("PASSED: decoded json string")
		except Exception as e:
			print('Failed to decode json: ',e)
			print(message[e.pos-50:e.pos+1000])

		return

	def get_data(self, listName, key):

		valList= []

		try:
			for i in self.jsonObj[listName]:
				valList.append(i[key])
		except IndexError as e:
			print(e, "   : get_data function")
			print('Trying to get the below data:\n',listName,key,subkey)
			print("Trying to get 0 index of json object")
			print(self.jsonObj)

		return valList


class Timelines:
	def __init__(self):
		pass

	def get_test_timelines(self):

		return ['Timeline ' + str(x) for x in range(1,2000)]


	def get_aux_timelines(self,ipaddress):
		'''
		retrieves timelines from Watchout

		'''

		message='getAuxTimelines\r'
		message=message.encode()

		# To ensure everything gets to Watchout

		BUFF_SIZE = 4096
		PORT = 3040

		#try 5 times to connect..
		for i in range(5):
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				#s.setblocking(False)
				s.connect((ipaddress,PORT))

				break

			except socket.error as e:
				print('Attempt {attemptNum} at connecting to Watchout'.format(attemptNum=i))
				print(e)

		'''
		ensure we get everything
		keep sending until everything has successfully been sent..

		'''
		MSGLEN = len(message)
		totalSent = 0


		while totalSent < MSGLEN:
			try:
				sent = s.send(message[totalSent:])
			except socket.error as e:
				print('Error with connection:  ',e)
				break

			totalSent+= sent

		# we are using this string to confirm we received everything
		#this is always the end of the json data when getting timeline data
		end = b'\r\n}\r\n]\r\n}\r\n'
		endLen = len(end)
		total_data=[]

		#keep going until we've found 'end' in any part of the received data
		while True:
			data = s.recv(BUFF_SIZE)

			if end in data:
				total_data.append(data)
				break

			total_data.append(data)

			if len(total_data)>1:
				#the data may have been split between two sends
				last_pair=total_data[-2]+total_data[-1]

				if end in last_pair:
					total_data[-2]=last_pair[:last_pair.find(end)] #search in the last bit of data for the end string
					#total_data.pop()
					break


		s.close()

		finalData=''
		for x in total_data:
			finalData += x.decode()

		'''

		The data looks like this -
		{ItemList:['Name':['Timeline1','Timeline2']]}
		Our keys are just ItemList and then Name. It also sends back the
		duration but we don't care about that. The duration is not useful
		at all unless you make the duration of the timeline EXACTLY the same
		as the end of the cue. I don't see how that's useful at all

		'''
		jsonObj=json_parser()
		jsonObj.decode(finalData[6:]) #strip off the 'Reply '
		names = jsonObj.get_data('ItemList','Name')
		#pprint.pprint(names)

		return names