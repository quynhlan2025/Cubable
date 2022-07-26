from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.utils import logger
from src.utils.element import wait_for_element_displayed, send_keys, find_elements


class SearchPage:
    __TEXTBOX_SEARCH = (By.CSS_SELECTOR, "[type='search']")
    __ITEM_SEARCH_RESULT = (By.CSS_SELECTOR, ".product-name")
    __TITLE_PAGE = (By.CSS_SELECTOR, ".sc-bRBYWo")

    def wait_for_homepage_is_loaded(self):
        wait_for_element_displayed(self.__TITLE_PAGE)

    def type_search_key(self, search_key):
        wait_for_element_displayed(self.__TEXTBOX_SEARCH)
        send_keys(self.__TEXTBOX_SEARCH, search_key, press_enter=True, clear=True)
        logger.info(f"Type : '{search_key}'")

    def get_list_search_result(self) -> list[WebElement]:
        list_element = find_elements(self.__ITEM_SEARCH_RESULT)
        return list_element
