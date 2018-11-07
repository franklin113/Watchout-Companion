from base import Base
from pages import Pages
import pprint

class Bank(Base):


	def __init__(self,timelineNames):
		self.timelineList = timelineNames
		#print(self.timelineList)
		self.dictOfPages = {str(pageCounter): {} for pageCounter in range(1,100) }
		self.dictOfActionPages = {str(pageCounter): {} for pageCounter in range(1,int(len(self.timelineList)/12))}
		#print(self.dictOfPages)
		self.splitTimelineList = self.split_timelines()
		#self.split_timelines()
		self.add_timelines_to_dict()

	def split_timelines(self):
		'''


		'''
		counter = 1
		pageCounter = 1
		newTimelineList=[] # a list of lists
		curTimelineList = []
		composite_list = [self.timelineList[x:x+12] for x in range(0, len(self.timelineList),12)]
		#print(composite_list)
		'''
		for x in self.timelineList:

			#print(x)
			if counter < 12:
				curTimelineList.append(x)

			else:
				#print(newTimelineList)
				buttonPages = Pages(newTimelineList,'buttons')
				actionPages = Pages(newTimelineList,'actions')
				self.dictOfPages[str(pageCounter)] = buttonPages.get_items()
				print('dict of pages: ',self.dictOfPages)
				self.dictOfActionPages[str(pageCounter)] = actionPages.get_items()
				newTimelineList.clear()
				pageCounter += 1
				counter = 0
				#print('page counter: ',pageCounter)
				#print('Page # ',counter)
			counter += 1
		self.splitTimelineList.append()
		'''
		return composite_list

	def add_timelines_to_dict(self):
		pageCounter = 1
		for i in self.splitTimelineList:
			#pprint.pprint('in bank: add_timelines '+str(i))
			buttonPages = Pages(i,'buttons')
			actionPages = Pages(i,'actions')
			self.dictOfPages[str(pageCounter)] = buttonPages.get_items()
			self.dictOfActionPages[str(pageCounter)] = actionPages.get_items()
			pageCounter += 1

	def print(self):
		print('Button Pages: ')
		pprint.pprint(self.dictOfPages)

		print('Action Pages: ')
		pprint.pprint(self.dictOfActionPages)

	def get_bank(self):
		return {'buttons':self.dictOfPages,'actions':self.dictOfActionPages}
def test():

	timelines = ['Timeline ' + str(x) for x in range(1,20)]
	b = Bank(timelines)
#
# test()