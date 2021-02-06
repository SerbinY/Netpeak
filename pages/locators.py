
from selenium.webdriver.common.by import By



class MainPageLocators():
    CAREER_BUTTON = (By.CSS_SELECTOR, ".blog")

class CareerPageLocators():
    HIRING_BUTTON = (By.CSS_SELECTOR, ".agree-btn .green-btn")

class HiringPageLocators():
    UPLOAD_FILE = (By.CSS_SELECTOR, "[name='up_file']")
    WARNING_TEXT = (By.CSS_SELECTOR, "#up_file_name .control-label")
    INPUT_NAME = (By.CSS_SELECTOR, "#inputName")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "#inputLastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#inputEmail")
    INPUT_PHONE = (By.CSS_SELECTOR, "#inputPhone")
    SELECT_YEAR = (By.CSS_SELECTOR, "[name = 'by']")
    SELECT_MONTH = (By.CSS_SELECTOR, "[name = 'bm']")
    SELECT_DAY = (By.CSS_SELECTOR, "[name = 'bd']")
    SEND_FORM_BUTTON = (By.CSS_SELECTOR, "#submit")
    HELP_BLOCK = (By.CSS_SELECTOR, ".help-block")
    COURSES_BUTTON = (By.CSS_SELECTOR, ".blog")
