

class Base:

	def build_pages(self,numPages):
		pageList= {x: {} for x in range(1,numPages)}
		#print(pageList)
		return pageList





def test():
	base = Base()
	base.build_pages(10)

#test()