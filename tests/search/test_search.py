import allure

from src.consts import consts
from src.pages.search_page import SearchPage
from src.utils import logger, common, json_util
from tests import MasterTest


class TCSEARCH(MasterTest):

    @allure.title("Verify the flow search ")
    def test(self):
        try:

            file_path = consts.PROJECT_ROOT + "/data/search_data.json"
            json_data = json_util.load(file_path)
            pr_data = json_data["tc01"]
            search_page = SearchPage()
            search_page.wait_for_homepage_is_loaded()
            search_page.type_search_key(pr_data["key_search"])
            list_element = search_page.get_list_search_result()
            for item in list_element:
                title = item.text.lower()
                if pr_data["key_search"].lower() in title:
                    assert True
                    break
                else:
                    assert False
        except Exception as ex:
            logger.error(ex)
            self.failures.append(ex)
        finally:
            self.screenshot_binary_data.append(self.save_screenshot())
