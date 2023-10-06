import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestDisplayShoppingList:
    def test_displayshoppinglist(self):
        shoplistbtn = self.driver.find_element(By.XPATH, "//span[@class='icon']")
        shoplistbtn.click()

        try:
            full_display = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[@id='shopping-list' and contains(@class, 'homepage-sidebar--open')]")))
            print("Shopping list is on full display.")
        except:
            print("Shopping list is collapsed.")
