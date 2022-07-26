import builtins

import pytest

from src.consts import consts, runtime
from src.pages.login import login_page

from src.utils import logger, file_util, common
from src.utils.browser_driver import create_chrome_driver


def pytest_addoption(parser):
    parser.addoption("--env", action="store")


@pytest.fixture(scope="session")
def before_all_tests(request):  # Before all tests, run this function one time only.
    print("\x00")  # print a non-printable character to break a new line on console
    logger.info("=== Start Pytest session ===")

    # Read environment from a parameter named 'env'
    env = str(request.config.getoption("--env"))
    config = file_util.read_properties_file(consts.ENV_CONFIG_FILE % env)
    file_util.create_folder(consts.SCREENSHOT_DIR.format(env))
    consts.ENV_CONFIG_FILE.format(env)
    file_util.delete_folder("allure-results")

    # Set global variables
    runtime.env = env

    # Init Chrome driver
    driver = create_chrome_driver(headless=False)
    builtins.driver = driver
    # Navigate to test site
    driver.get(config["url"])
    #login_page = LoginPage()
   # login_page.click_sign_up()
   # login_page.click_go_to_login()
   # login_page.wait_for_loginpage_is_loaded()
    login_page.type_user(config["username"])
    login_page.type_password(config["password"])
    login_page.click_sign_me_in_button()
    #login_page.click_on_button_login()

def pytest_sessionfinish(session):
    # Quit Chrome driver
    if hasattr(builtins, "driver"):
        getattr(builtins, "driver").quit()

    # Generate Allure report dir
    logger.info("=== End Pytest session ===")
