
'''
bank_actions -> actionPages -> Action (me)

example output -
'bank_actions': {'1': {'1': [{'action': 'run',
                               'id': 'HJtn6Dfj7',
                               'instance': 'B1M9CUzoX',
                               'label': 'B1M9CUzoX:run',
                               'options': {'timeline': '--  Backup image'}}],

'''

class Action():

	def __init__(self,timelineName):
		'''
		each physical button contains a button object and an action object.
		For every button, we are creating an action object to be added to
		the 'bank_action' key in our main dict.

		:param timelineName:
		'''

		self.info = [{
			'id':'HJtn6Dfj7',
			'label':"B1M9CUzoX:run",
			'instance':"B1M9CUzoX",
			'action':'run',
			'options': {'timeline':timelineName}
		}]
	def get_action(self):
		# returns our dictionary
		return self.info
