

class Button_Style:
	def __init__(self,timelineName):
		self.timelineName=timelineName

	def get_styles(self):
		self.styleDict = {'style':'text',
						  'size':'large',
						  'bgcolor':0,
						  'alignment':'center:center',
						  'color':16777215,
						  'text': self.timelineName}
		return self.styleDict


