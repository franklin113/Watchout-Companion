from base import Base
from Button import Button
from action import Action
class Pages(Base):
	def __init__(self,timelineNames, buttonOrAction):
		self.timelineNames = timelineNames
		self.infoDict = {}
		self.buttonOrAction = buttonOrAction

	def get_items(self):
		i=1
		if self.timelineNames == None or len(self.timelineNames)== 0:
			return {'none'}
		if len(self.timelineNames) > 12:
			print('Error: pass too many timelines to one page object')
			return {'too many timelines'}
		else:
			for timeline in self.timelineNames:
				if self.buttonOrAction == 'buttons':
					newButton = Button(timeline)
					self.infoDict[str(i)] = newButton.get_button()
				elif self.buttonOrAction == 'actions':
					newAction = Action(timeline)
					self.infoDict[str(i)] = newAction.get_action()
				i+= 1
		#print('within pages.py: ',self.infoDict)
		return self.infoDict