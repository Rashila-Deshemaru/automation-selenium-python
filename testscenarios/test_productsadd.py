import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestAddProductsToList:
    def test_add_product_to_list(self):

        product_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Red Capsicum , 500 gm']")))
        product_element.click()

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add to Shopping list')]")))

        # self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

        time.sleep(20)
        add_to_cart_button.click()


        product_name = self.driver.execute_script(
            "return document.querySelector('.list-create-card-ruled.list-create-card__has-items .media-body').textContent;")

        if "Red Capsicum , 500 gm" in product_name:
            print(f"Product added to the shopping list: {product_name}")
        else:
            print("Product not added to the shopping list.")