from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import logger
from src.utils.element import find_element, click, send_keys


class CollectionPage(BasePage):
    # Elements
    # --------
    __NEW_BUTTON = (By.CSS_SELECTOR, 'button.wgc-button.ml-15')
    __COLLECTION_ICON = (By.CSS_SELECTOR, '.icon.icon-collection')
    __COLLECT_ITEM_BY_NAME = (By.XPATH, '//*[contains(text(),\'Lan\')]')

    # ACTIONS
    # -------
    def get_results_header(self):
        element = find_element(self.__HEADING)
        return element.text

    def click_on_new_button(self):
        find_element(self.__NEW_BUTTON)
        click(self.__NEW_BUTTON)
        logger.info("Click on 'New' button")

    def click_on_collection_icon(self):
        click(self.__COLLECTION_ICON)
        logger.info("Click on 'Collection' icon on left menu")

    def click_on_collection_item(self):
        click(self.__COLLECT_ITEM_BY_NAME)
        logger.info("Click on 'Collection' by Name")


collection_page = CollectionPage()
