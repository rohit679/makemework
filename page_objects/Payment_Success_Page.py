"""
    This Object models the product page.
"""

from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Payment_Success_Page(Base_Page):
    "This class models the sunscreen page"
    def start(self):
        "Go to this URL -- if needed"
        url = "confirmation"
        self.open(url)