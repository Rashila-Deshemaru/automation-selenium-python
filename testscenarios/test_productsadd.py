
import pytest
from pages.merokirana_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestAddProductsToList:
    def test_add_product_to_list(self):
        lp = LaunchPage(self.driver, self.wait)
        lp.findproduct()


