import builtins
import unittest

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from src.consts import consts, runtime
from src.utils import logger, file_util, datetime_util


@pytest.mark.usefixtures("before_all_tests")
class MasterTest(unittest.TestCase):
    failures = []
    screenshot_file = ""
    screenshot_binary_data = []
    start_time = 0

    @property
    def driver(self) -> WebDriver:
        return getattr(builtins, "driver")

    def setUp(self):  # Before each test case
        self.start_time = datetime_util.current_time()
        test_case_name = self.__class__.__name__.lower()

        # Setup a screenshot dir for each test case
        screenshot_tc_dir = consts.SCREENSHOT_TC_DIR.format(runtime.env, test_case_name)
        file_util.delete_folder(screenshot_tc_dir)
        file_util.create_folder(screenshot_tc_dir)
        self.screenshot_binary_data.clear()
        self.screenshot_file = screenshot_tc_dir + consts.SCREENSHOT_FILE.format(test_case_name)
        logger.info(f"Start test case: {test_case_name}")

    def tearDown(self):  # After each test case
        def list2reason(exc_list):  # function to process error/failure
            if exc_list and exc_list[-1][0] is self:
                return exc_list[-1][1]
            return None

        result = self.defaultTestResult()  # get result of the test case
        self._feedErrorsToResult(result, self._outcome.errors)
        error = list2reason(result.errors)  # count the number of errors failed by script/code
        failure = list2reason(result.failures)  # count the number of failures failed by test assertion
        # Final result of the test case: no error, no failure
        is_test_passed = not error and not failure

        elapsed_time = (datetime_util.current_time() - self.start_time).total_seconds()
        logger.info("-----------")
        logger.info("Test status: PASSED") if is_test_passed else logger.warning("Test status: FAILED")
        logger.info("Time taken : " + datetime_util.pretty_time(elapsed_time))
        for data in self.screenshot_binary_data:
            allure.attach(name="screenshot", body=data, attachment_type=allure.attachment_type.PNG)
        assert is_test_passed and self.failures == []

    def save_screenshot(self):
        self.driver.save_screenshot(self.screenshot_file)  # save screenshot to 'reports' folder
        return self.driver.get_screenshot_as_png()  # save the screenshot for Allure attachment
