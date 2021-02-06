from .base_page import BasePage


class SchoolPage(BasePage):

    def should_be_school_url(self):
        assert "school" in self.browser.current_url, "Нужная страница не открыта"
