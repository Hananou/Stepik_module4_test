from .base_page import BasePage

class MainPage(BasePage):
    def go_to_login_page(self):
        link = browser.find_element_by_css_selector("#login_link")
        link.click() 