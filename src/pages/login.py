from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utils import logger
from src.utils.element_util import find_elements, send_keys, click


class LoginPage(BasePage):
    # Elements
    # --------
    __USER_INPUT = (By.CSS_SELECTOR, "[type=\"email\"]")
    __PASSWORD_INPUT = (By.CSS_SELECTOR, "[type=\"password\"]")
    __SIGN_ME_IN_BUTTON = (By.CSS_SELECTOR, "div.wgc-button__content")
    __avatar = (By.CSS_SELECTOR, "[src=\"assets/images/logos/logo.png\"]")

    # Actions
    # -------

    def type_user(self, username):
        send_keys(self.__USER_INPUT, username)
        logger.info("Type user: " + username)

    def type_password(self, password):
        send_keys(self.__PASSWORD_INPUT, password)
        logger.info(f"Type password: {password}")

    def click_sign_me_in_button(self):
        click(self.__SIGN_ME_IN_BUTTON)
        logger.info("Click 'Sign me in' button")

    def verify_avatar(self):
        element = find_elements(self.__avatar)
        logger.info(" avatar is displayed")
        return element.is_displayed()

    def login(self, username, password):
        self.type_user(username)
        self.type_password(password)
        self.click_sign_me_in_button()


login_page = LoginPage()
