from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage)
    def add_product_to_basket
        add_to_busket_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        add_to_busket_link.click()