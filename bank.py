from pages import Pages
import pprint

'''
A bank object generates both the "bank_actions" and the "bank" portions of the data

example -
{'bank': {'1': {'1': {'alignment': 'center:center',
                      'bgcolor': 0,
                      'color': 16777215,
                      'size': 'large',
                      'style': 'text',
                      'text': '--  Backup image'},


'bank_actions': {'1': {'1': [{'action': 'run',
                               'id': 'HJtn6Dfj7',
                               'instance': 'B1M9CUzoX',
                               'label': 'B1M9CUzoX:run',
                               'options': {'timeline': '--  Backup image'}}],



'''


class Bank():
	def __init__(self,timelineNames):
		self.timelineList = timelineNames
		self.dictOfPages = {str(pageCounter): {} for pageCounter in range(1,100) }
		self.dictOfActionPages = {str(pageCounter): {} for pageCounter in range(1,int(len(self.timelineList)/12))}
		self.splitTimelineList = self.split_timelines()
		self.add_timelines_to_dict()

	def split_timelines(self):
		# each page object can only contain 12 buttons (12 timelines)
		# split the timeline list into a list of lists, each containing
		# only 12 timelines at a time.

		composite_list = [self.timelineList[x:x+12] for x in range(0, len(self.timelineList),12)]

		return composite_list

	def add_timelines_to_dict(self):
		# loop through the split up timeline list and create buttons
		# for each timeline. Every new list is a new page.

		# example data-  {'1': {'1': (...button...}
		#			 	  '2': {'1': {...button...}

		pageCounter = 1
		for i in self.splitTimelineList:
			buttonPages = Pages(i,'buttons') # passing in buttons so it creates a button page
			actionPages = Pages(i,'actions') # passing in actions so it creates an action page
			self.dictOfPages[str(pageCounter)] = buttonPages.get_items()
			self.dictOfActionPages[str(pageCounter)] = actionPages.get_items()
			pageCounter += 1

		return

	def print(self):
		print('Button Pages: ')
		pprint.pprint(self.dictOfPages)

		print('Action Pages: ')
		pprint.pprint(self.dictOfActionPages)

	def get_bank(self):
		return {'buttons':self.dictOfPages,'actions':self.dictOfActionPages}

