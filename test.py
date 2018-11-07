from bank import Bank
from pages import Pages
from timelines import Timelines



def test_bank(timelines = None):
	timelines = timelines
	if timelines == None:
		newTimelines = Timelines()
		timelines = newTimelines.get_test_timelines()
	bank = Bank(timelines)
	bank.print()
	print("Debug: Bank-")
	print('Bank: PASSED')

def test_page():
	print('Debug: Page-')

	page = Pages(['Timeline1','Timeline2'],'button')

	print('Page: Full page- PASSED   ',page.get_items())

	page2 = Pages(None,None)

	print('Page: Empty page- PASSED   ',page2.get_items())

	x = [str(x) for x in range(20)]

	page3 = Pages(x,'button')
	print('Page: 11+ pages- PASSED   ',	page3.get_items())

def test_timelines():
	t = Timelines()
	newTimelines = t.get_aux_timelines('127.0.0.1')
	print(newTimelines)
	return newTimelines

#test_base()
#test_page()

myTimelines = test_timelines()

test_bank(myTimelines)
