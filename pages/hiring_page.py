
from .base_page import BasePage
import os
from .locators import HiringPageLocators
from selenium.webdriver.support.ui import Select
import time



class HiringPage(BasePage):
    def download_png(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_name = "PNG94.png"
        file_path = os.path.join(current_dir, file_name)
        elemet = self.browser.find_element(*HiringPageLocators.UPLOAD_FILE)
        elemet.send_keys(file_path)
        time.sleep(5)

    def check_warning(self):
        warning_text = self.browser.find_element(*HiringPageLocators.WARNING_TEXT).text
        assert "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)." == warning_text,\
        "Отсутствует или не верное сообщение об ошибке"

    def fill_block_3(self):
        self.browser.find_element(*HiringPageLocators.INPUT_NAME).send_keys("Евгений")
        self.browser.find_element(*HiringPageLocators.INPUT_LAST_NAME).send_keys("Сербин")
        self.browser.find_element(*HiringPageLocators.INPUT_EMAIL).send_keys("yevgenserbin@gmail.com")
        self.browser.find_element(*HiringPageLocators.INPUT_PHONE).send_keys("+380977438474")
        Select(self.browser.find_element(*HiringPageLocators.SELECT_YEAR)).select_by_visible_text("1986")
        Select(self.browser.find_element(*HiringPageLocators.SELECT_MONTH)).select_by_visible_text("сентября")
        Select(self.browser.find_element(*HiringPageLocators.SELECT_DAY)).select_by_visible_text("29")

    def send_form(self):
        self.browser.find_element(*HiringPageLocators.SEND_FORM_BUTTON).click()

    def check_color_help_block(self):
        assert self.browser.find_element(*HiringPageLocators.HELP_BLOCK).value_of_css_property("color") == "rgba(255, 0, 0, 1)",\
        "Сообщение 'Все поля являются обязательными для заполнения' не подсвечено красным цветом"

    def go_to_school_page(self):
        self.browser.find_element(*HiringPageLocators.COURSES_BUTTON).click()
