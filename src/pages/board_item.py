from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import element_util, logger
from src.utils.element import click, send_keys, wait_element_invisible, wait_for_elements_displayed, find_element


class BoardItemPage(BasePage):
    # Elements
    # --------
    __HEADING = (By.CSS_SELECTOR, 'div[data-attrid="title"] span[role="heading"]')
    __INSERT_ROW_BUTTON = (By.CSS_SELECTOR, ".inserting-row__left button")
    __ITEM_NAME_INPUT = (By.CSS_SELECTOR, "[placeholder=\"Type a name\"]")
    __ICON_LOADING_IN_ROW=(By.CSS_SELECTOR,'.row-cells .row-cell wgc-loading')
    __COLUMN_NAME=(By.XPATH,'//div[contains(@class,\'wgc-basic-button__content\')]//span[text() = \'item name123:\']')
    # ACTIONS
    # -------
    def get_results_header(self):
        element = element_util.find_element(self.__HEADING)
        return element.text

    def click_on_insert_row_button(self):
        click(self.__INSERT_ROW_BUTTON)
        logger.info(f"Click on button insert item ")

    def enter_item_name(self, text):
        send_keys(self.__ITEM_NAME_INPUT, text, press_enter=True, clear=False)
        logger.info(f" enter : {text} in textbox ")
        wait_element_invisible(self.__ICON_LOADING_IN_ROW)
        logger.info(f"  wait for icon loading in row invisible ")

    def is_column_diplayed(self,text):
        try:
            element = find_element(self.__COLUMN_NAME)
            logger.info(f" check column is displayed")
        except:
            return False
        finally:
            return element.is_displayed()



board_item_page = BoardItemPage()
