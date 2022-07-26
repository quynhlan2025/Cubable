from selenium.webdriver.common.by import By

from src.utils import logger
from src.utils.element import click, send_keys, wait_for_element_displayed, find_element


class LoginPage:
    # Elements
    # --------
    __EMAIL = (By.ID, "email")
    __PASSWORD_INPUT = (By.ID, "password")
    __SIGN_ME_IN_BUTTON = (By.XPATH, "//button[text()='Sign me in']")

    __SIGN_UP=(By.CSS_SELECTOR,"[href=\"/signup\"]")
    __GO_TO_LOGIN=(By.CSS_SELECTOR,".sc-htoDjs.kdHsSl")
    __BUTTON_LOGIN=(By.CSS_SELECTOR,".sc-htoDjs.fPyuUJ")
    # Actions
    # -------
    __TITLE_LOGIN_PAGE=(By.CSS_SELECTOR,".hgmibr")

    def type_user(self, user):
        wait_for_element_displayed(self.__EMAIL)
        send_keys(self.__EMAIL, user)
        logger.info(f"Type user id: '{user}'")

    def type_password(self, password):
        send_keys(self.__PASSWORD_INPUT, password)
        logger.info(f"Type password: '{password}'")

    def click_sign_up(self):
        click(self.__SIGN_UP)
        logger.info("Click 'Sign up' button")

    def click_on_button_login(self):
        click(self.__BUTTON_LOGIN)
        logger.info(f"Click  button Login")

    def click_go_to_login(self):
        click(self.__GO_TO_LOGIN)
        logger.info(f"Click go to login")

    def wait_for_loginpage_is_loaded(self):
        wait_for_element_displayed(self.__TITLE_LOGIN_PAGE)

