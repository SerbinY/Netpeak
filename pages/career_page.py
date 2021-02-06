
from .base_page import BasePage
from .locators import CareerPageLocators



class CareerPage(BasePage):
    def go_to_hiring_page(self):
        self.browser.find_element(*CareerPageLocators.HIRING_BUTTON).click()
