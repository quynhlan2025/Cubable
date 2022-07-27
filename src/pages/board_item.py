from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import element_util, logger, string_util
from src.utils.element import click, send_keys, wait_element_invisible, wait_for_elements_displayed, find_element


class BoardItemPage(BasePage):
    # Elements
    # --------
    __HEADING = (By.CSS_SELECTOR, 'div[data-attrid="title"] span[role="heading"]')
    __INSERT_ROW_BUTTON = (By.CSS_SELECTOR, ".inserting-row__left button")
    __ITEM_NAME_INPUT = (By.CSS_SELECTOR, "[placeholder=\"Type a name\"]")
    __ICON_LOADING_IN_ROW = (By.CSS_SELECTOR, '.row-cells .row-cell wgc-loading')
    __COLUMN_NAME = (
        By.XPATH, '//div[contains(@class,\'wgc-basic-button__content\')]//span[text() = \'%s\']')
    __COLUMN_ADD_ICON = (By.CSS_SELECTOR, ".last-cell button")
    __FIELD_TYPE = (By.XPATH, "//span[text()='Text']/../../..")

    # POP UP NEW FIELD
    __FIELD_NAME_INPUT = (By.CSS_SELECTOR, "[placeholder=\"Type a name\"]")
    __FIELD_NAME_DESCRIPTON_INPUT = (By.CSS_SELECTOR, "[placeholder=\"Type description\"]")
    __FIELD_NAME_VALUE = (By.CSS_SELECTOR, "[placeholder=\"Type a value\"]")
    __BUTTON_CREATE = (By.CSS_SELECTOR, "[type=\"submit\"]")
    # BOARD TABLE
    __HEAD_COLUMN = (By.XPATH, "//span[contains(text(),'%s')]/../../self::*[contains(@class, 'name-handle')]")

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

    def is_field_value_displayed(self, text):
        try:
            new_xpath_element=string_util.cook_element(self.__COLUMN_NAME,text)
            element = find_element(new_xpath_element)
            logger.info(f" check column is displayed")
        except:
            return False
        finally:
            return element.is_displayed()

    def is_new_field_isdisplayed(self, header_name):
        try:
            new_xpath_locator = string_util.cook_element(self.__HEAD_COLUMN, header_name)
            element = find_element(new_xpath_locator)

            logger.info(f" check column {header_name} is created successfully")
        except:
            return False
        finally:
            return element.is_displayed()

    def click_on_add_column_icon(self):
        click(self.__COLUMN_ADD_ICON)
        logger.info(f" Click on add column icon ")

    def click_on_field_type(self):
        click(self.__FIELD_TYPE)
        logger.info(f" Click on field text")

    def enter_field_name(self, text):
        send_keys(self.__FIELD_NAME_INPUT, text)
        logger.info(f" enter {text}  to textbox field name")

    def enter_field_description(self, text):
        send_keys(self.__FIELD_NAME_DESCRIPTON_INPUT, text)
        logger.info(f" enter {text}  to textbox description field")

    def click_on_create_button(self):
        click(self.__BUTTON_CREATE)
        logger.info(f"click on create button")


board_item_page = BoardItemPage()
