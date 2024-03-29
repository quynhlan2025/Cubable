from src.pages.board import board_page
from src.pages.board_item import board_item_page
from src.pages.collection import collection_page
from src.utils import common
from tests import MasterTest


class BoardItemTest(MasterTest):

    def test_add_new_board(self):
        collection_page.click_on_collection_icon()
        collection_page.click_on_collection_item()
        board_page.click_on_add_new_board()
        board_page.type_on_board_name("board A")
        assert board_page.get_title_new_board() == "board A"
        # Verify new board is added
        board_item_page.click_on_insert_row_button()
        common.sleep(2)
        board_item_page.enter_item_name("item name123:")
        common.sleep(2)
        assert board_item_page.is_field_value_displayed("item name:") == True
        board_item_page.click_on_add_column_icon()
        common.sleep(5)
        board_item_page.click_on_field_type()
        common.sleep(1)
        board_item_page.enter_field_name("Textbox")
        board_item_page.enter_field_description("Textbox")
        board_item_page.click_on_create_button()
        common.sleep(1)
        assert board_item_page.is_new_field_isdisplayed("Textbox")
        common.sleep(1)

        pass
