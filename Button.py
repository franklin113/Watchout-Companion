from base import Base
from buttonStyle import Button_Style

class Button(Base):
    def __init__(self,timelineName):
        self.timelineName = timelineName
        self.button = self.get_button()

    def get_button(self):
        self.buttonStyle = Button_Style(self.timelineName)
        return self.buttonStyle.get_styles()
