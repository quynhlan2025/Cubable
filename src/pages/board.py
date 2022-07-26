from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import element_util, logger
from src.utils.element import click, wait_for_element_displayed, send_keys


class BoardPage(BasePage):
    # Elements
    # --------
    __HEADING = (By.CSS_SELECTOR, 'div[data-attrid="title"] span[role="heading"]')
    __ADD_NEW_BOARD_BUTTON = (By.CSS_SELECTOR, 'div.mt-10 button')
    __BOARD_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="Type a name"]')
    __BOARD_TITLE = (By.CSS_SELECTOR, 'h2.wgc-inline-input span')

    # ACTIONS
    # -------
    def get_results_header(self):
        element = element_util.find_element(self.__HEADING)
        return element.text

    def click_on_add_new_board(self):
        click(self.__ADD_NEW_BOARD_BUTTON)
        logger.info(f"Click on add new board button")

    def wait_for_board_page_is_loaded(self):
        wait_for_element_displayed(self.__ADD_NEW_BOARD_BUTTON)
        logger.info(f"Wait for button add new board displayed")

    def type_on_board_name(self, text):
        send_keys(self.__BOARD_NAME_INPUT, text, press_enter=True, clear=True)
        logger.info(f"Enter board name: {text} into textbox ")

    def get_title_new_board(self):
        element = element_util.find_element(self.__BOARD_TITLE)
        return element.text


board_page = BoardPage()
