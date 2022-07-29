from src.pages.collection import collection_page
from src.pages.login import login_page
from src.utils import common
from tests import MasterTest


class CollectionTest(MasterTest):

    def test_add_new_collection(self):

        common.sleep(5)
        collection_page.click_on_collection_icon()
        collection_page.click_on_collection_item()
        common.sleep(1)
        collection_page.click_on_new_button()


pass
