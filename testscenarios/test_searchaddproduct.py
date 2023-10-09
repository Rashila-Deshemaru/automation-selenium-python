import pytest
from pages.merokirana_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
class TestSearchAddProduct:

    def test_search_add_product(self):
        lp = LaunchPage(self.driver, self.wait)
        lp.searchproduct("rice")