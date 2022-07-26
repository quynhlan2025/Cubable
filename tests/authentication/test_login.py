from src.pages.login import login_page
from src.utils import logger, common
from tests.base_test import BaseTest


class LoginTest(BaseTest):

    def test_login_successful(self):
        # Test data
        ...

        # Test steps
        login_page.type_user("lan.nguyen@cubable.com")
        login_page.type_password("12345678L@n")
        login_page.click_sign_me_in_button()
        assert login_page.verify_avartar() == True
        logger.info(" avatar is displayed")
        common.sleep(5)
        ...

        # Test cleanup
        ...
