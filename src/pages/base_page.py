from selenium.webdriver.support.select import Select

from src.utils import logger


class BasePage:


    def go_to_url(self, urL):
        pass

    def select_dropdown(self, name, element, option_value):
        logger.info(f"Select dropdown '{name}' with value '{option_value}'")
        select = Select(element)
        select.select_by_visible_text(option_value)

