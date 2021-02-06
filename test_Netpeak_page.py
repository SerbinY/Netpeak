from pages.main_page import MainPage
from pages.career_page import CareerPage
from pages.hiring_page import HiringPage
from pages.school_page import SchoolPage



def test_task_Netpeak(browser):
     link = "https://netpeak.ua/"
     page = MainPage(browser, link)
     page.open()
     page.go_to_career_page()
     career_page = CareerPage (browser, browser.current_url)
     career_page.go_to_hiring_page()
     hiring_page = HiringPage (browser, browser.current_url)
     hiring_page.download_png()
     hiring_page.check_warning()
     hiring_page.fill_block_3()
     hiring_page.send_form()
     hiring_page.check_color_help_block()
     hiring_page.go_to_school_page()
     school_page = SchoolPage (browser, browser.current_url)
     school_page.should_be_school_url()

