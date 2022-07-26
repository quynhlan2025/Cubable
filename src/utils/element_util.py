import builtins

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exc
from selenium.webdriver.support.wait import WebDriverWait

DEFAULT_TIMEOUT = 10  # seconds


def find_element(element: tuple, timeout=DEFAULT_TIMEOUT, wait=True) -> WebElement:
    """
    Find an element existing in DOM with a timeout in seconds.
    :return: WebElement if found
    :raise: NoSuchElementException if not found
    """
    driver = getattr(builtins, "driver")
    locator = element[0]
    value = element[1]
    try:
        if wait:
            return WebDriverWait(driver, timeout).until(exc.visibility_of_element_located((locator, value)))
        return driver.find_element(locator, value)
    except Exception:
        log = "Element not found with locator %s value '%s' after %d seconds" % (locator, value, timeout)
        raise NoSuchElementException(log)


def find_elements(element: tuple, timeout=60, wait=True):
    """
    Find an available element list with a timeout in seconds.
    :return: WebElement if found
    :raise: NoSuchElementException if not found
    """
    driver: WebDriver = getattr(builtins, "driver")
    locator = element[0]
    value = element[1]
    try:
        if wait:
            return WebDriverWait(driver, timeout).until(exc.visibility_of_element_located((locator, value)))
        return driver.find_elements(locator, value)
    except Exception:
        log = "Element not found with locator %s value '%s' after %d seconds" % (locator, value, timeout)
    raise NoSuchElementException(log)


def send_keys(element: tuple, value: str, press_enter=False, clear=False):
    ele = find_element(element)
    if clear:
        ele.clear()
    ele.send_keys(value)
    if press_enter:
        ele.send_keys(Keys.ENTER)


def click(element: tuple):
    find_element(element).click()

def takeScreenshot(self, text):
    allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
    pass