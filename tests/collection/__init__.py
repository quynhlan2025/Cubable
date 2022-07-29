import unittest

import pytest


@pytest.mark.usefixtures("before_all_suite")
class BoardTest(unittest.TestCase):
    def create_a_board(self):
        pass

    pass
