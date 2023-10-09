import pytest
from pages.merokirana_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
class TestlistShoppingitems:
    def test_list_shopping_items(self):
        lp = LaunchPage(self.driver, self.wait)
        lp.findproduct()
        lp.searchproduct("rice")
        lp.listproductname()