import time
import re
import pytest
from pages.product_details_page import ProductPage
from pages.merokirana_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestOperationOnCart:
    def test_operation_on_cart(self):
        pdt = ProductPage(self.driver, self.wait)

        lp = LaunchPage(self.driver, self.wait)
        lp.findproduct()

        pdt.increaseqnty()
        pdt.increaseqnty()
        pdt.decreaseqnty()
        pdt.clearshoppinglist()








