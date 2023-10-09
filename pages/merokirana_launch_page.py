import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class LaunchPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait


    def findproduct(self):
        product_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Mr. Muscle Kitchen Cleaner, 450ml']")))
        product_element.click()

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add to Shopping list')]")))

        # self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

        time.sleep(20)
        add_to_cart_button.click()

        product_name = self.driver.execute_script(
            "return document.querySelector('.list-create-card-ruled.list-create-card__has-items .media-body').textContent;")

        if "Mr. Muscle Kitchen Cleaner, 450ml" in product_name:
            print(f"Product added to the shopping list: {product_name}")
        else:
            print("Product not added to the shopping list.")


    def searchproduct(self, searchname):

        search_bar = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='global_search']")))
        search_bar.click()
        search_bar.clear()

        search_bar.send_keys(searchname)
        search_bar.send_keys(Keys.RETURN)

        product_single = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-card__image-holder']")))
        product_single.click()

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add to Shopping list')]")))

        # self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

        initial_shopping_list_content = self.driver.find_element(By.ID, 'shopping-list').text

        time.sleep(10)
        add_to_cart_button.click()
        time.sleep(5)

        updated_shopping_list_content = self.driver.find_element(By.ID, 'shopping-list').text

        if initial_shopping_list_content != updated_shopping_list_content:
            print(f"Product added to the shopping list.")
        else:
            print("Product not added to the shopping list.")

    def listproductname(self):
        listproduct = self.driver.find_elements(By.XPATH,
                                                "//div[@class='list-create-card__list-item list-create-card-ruled list-create-card__has-items']")

        product_names = set()

        for item in listproduct:
            product_name_element = item.find_element(By.XPATH, ".//div[@class='media-body']")
            product_name = product_name_element.text

            if product_name not in product_names:
                print(f"Product Name: {product_name}")
                product_names.add(product_name)



