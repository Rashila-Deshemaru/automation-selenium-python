import time
import re
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.cart_parent_element = None
        self.product_quantity = None

    # to increase quantity

    def increaseqnty(self):
        cart_parent_locator = (By.XPATH, "//div[@id='shopping-list' and contains(@class, 'homepage-sidebar--open')]")
        self.cart_parent_element = self.wait.until(EC.visibility_of_element_located(cart_parent_locator))

        plus_button_locator = self.cart_parent_element.find_element(By.CLASS_NAME, "product-qty__btn--plus")
        plus_button = self.wait.until(EC.element_to_be_clickable(plus_button_locator))

        self.driver.execute_script("arguments[0].scrollIntoView();", plus_button)
        action = ActionChains(self.driver)
        action.move_to_element(plus_button).click().perform()

        time.sleep(5)

        productqnty = self.cart_parent_element.find_element(By.CLASS_NAME, "product-qty__input")
        product_quantity = productqnty.get_attribute("value")
        self.product_quantity = int(product_quantity)
        print("New product quantity", product_quantity)

        newprice_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-create-card__price")))
        newprice_text = newprice_element.text.strip()
        newnumeric_price_match = re.search(r'\d+', newprice_text)
        newnumeric_price = int(newnumeric_price_match.group())
        print("Old Price:", newnumeric_price)

        oldprice_element = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "list-create-card__item-price")))
        oldprice_text = oldprice_element.text.strip()
        oldnumeric_price_match = re.search(r'\d+', oldprice_text)
        oldnumeric_price = int(oldnumeric_price_match.group())
        print("New Price:", oldnumeric_price)

        if newnumeric_price > oldnumeric_price:
            print(f"product quantity increased to {product_quantity}")
        else:
            print("Quantity has not changed.")

    # decrease quantity
    def decreaseqnty(self):
        cart_parent_locator = (By.XPATH, "//div[@id='shopping-list' and contains(@class, 'homepage-sidebar--open')]")
        self.cart_parent_element = self.wait.until(EC.visibility_of_element_located(cart_parent_locator))

        minus_button_locator = self.cart_parent_element.find_element(By.CLASS_NAME, "product-qty__btn--minus")
        minus_button = self.wait.until(EC.element_to_be_clickable(minus_button_locator))

        action = ActionChains(self.driver)
        action.move_to_element(minus_button).click().perform()

        time.sleep(10)

        productqnty = self.cart_parent_element.find_element(By.CLASS_NAME, "product-qty__input")
        product_quantity_updated = productqnty.get_attribute("value")
        if self.product_quantity is None:
            self.product_quantity = int(product_quantity_updated)  # Set product_quantity initially

        # Compare the updated quantity with the previous quantity
        if int(product_quantity_updated) < self.product_quantity:
            self.product_quantity = int(product_quantity_updated)  # Update the class attribute
            print(f"Product quantity decreased to {self.product_quantity}")
        else:
            print("Quantity has not changed.")


    # to clear entire shopping list
    def clearshoppinglist(self):
        self.driver.execute_script("arguments[0].scrollTo(0, 0);", self.cart_parent_element)

        clearbtn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@title, 'Clear this list')]")))
        clearbtn.click()

        modal_locator = (By.ID, "CLEAR_MODAL")
        modal = self.wait.until(EC.visibility_of_element_located(modal_locator))

        modal_msg = self.wait.until(EC.presence_of_element_located((By.ID, "exampleModalLabel")))
        modal_title = modal_msg.text
        print(modal_title)

        no_button = modal.find_element(By.XPATH, "//button[contains(text(), 'No, thanks!')]")
        no_button.click()
        time.sleep(5)
        products_inlist = self.driver.execute_script(
            "return document.querySelector('.list-create-card__has-items') !== null;")
        if products_inlist:
            print("no thanks is clicked and list is not empty")

        clearbtn.click()
        modal = self.wait.until(EC.visibility_of_element_located(modal_locator))

        yes_button = modal.find_element(By.XPATH, "//button[contains(text(), 'Yes, I am sure!')]")
        yes_button.click()
        time.sleep(5)
        products_inlist = self.driver.execute_script(
            "return document.querySelector('.list-create-card__has-items') == null;")
        if products_inlist:
            print("Yes is clicked and list is empty")
