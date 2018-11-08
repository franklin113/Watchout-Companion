

'''
bank -> page -> Button (me)

example output -
          '2': {'1': {'alignment': 'center:center',
                      'bgcolor': 0,
                      'color': 16777215,
                      'size': 'large',
                      'style': 'text',
                      'text': 'Timeline 13'},

'''


class Button():
    def __init__(self,timelineName):
        self.timelineName = timelineName
        self.buttonDict = {'style':'text',
                  'size':'large',
                  'bgcolor':0,
                  'alignment':'center:center',
                  'color':16777215,
                  'text': self.timelineName}
    def get_button(self):

        return self.buttonDict
