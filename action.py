from base import Base



class Action(Base):

	def __init__(self,timelineName):
		self.id = 'HJtn6Dfj7'
		self.label = "B1M9CUzoX:run"
		self.instance = "B1M9CUzoX"
		self.action = 'run'
		self.options = {'timeline':timelineName}

	def get_action(self):
		info = [{
			'id':self.id,
			'label':self.label,
			'instance':self.instance,
			'action':self.action,
			'options':self.options
		}]
		return info

def test():
	a = Action('Timeline 1')
	print(a.get_action())


#test()