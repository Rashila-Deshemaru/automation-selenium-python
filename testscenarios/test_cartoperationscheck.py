import time
import re
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class TestOperationOnCart:
    def test_operation_on_cart(self):

        # add product to shopping list
        product_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Red Capsicum , 500 gm']")))
        product_element.click()

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add to Shopping list')]")))

        # self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)

        time.sleep(10)

        add_to_cart_button.click()

        # check if shopping list is empty
        products_added = self.driver.execute_script(
            "return document.querySelector('.list-create-card__has-items') !== null;")

        if products_added:
            print("shopping list is not empty")

        else:
            print("shopping list is empty")

        time.sleep(5)

        # to increase quantity
        cart_parent_locator = (By.XPATH, "//div[@id='shopping-list' and contains(@class, 'homepage-sidebar--open')]")
        cart_parent_element = self.wait.until(EC.visibility_of_element_located(cart_parent_locator))

        plus_button_locator = cart_parent_element.find_element(By.CLASS_NAME, "product-qty__btn--plus")
        plus_button = self.wait.until(EC.element_to_be_clickable(plus_button_locator))

        self.driver.execute_script("arguments[0].scrollIntoView();", plus_button)
        action = ActionChains(self.driver)
        action.move_to_element(plus_button).click().perform()

        time.sleep(5)

        productqnty = cart_parent_element.find_element(By.CLASS_NAME, "product-qty__input")
        product_quantity = productqnty.get_attribute("value")
        print("New product quantity", product_quantity)

        newprice_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-create-card__price")))
        newprice_text = newprice_element.text.strip()
        newnumeric_price_match = re.search(r'\d+', newprice_text)
        newnumeric_price = int(newnumeric_price_match.group())
        print("Old Price:", newnumeric_price)

        oldprice_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-create-card__item-price")))
        oldprice_text = oldprice_element.text.strip()
        oldnumeric_price_match = re.search(r'\d+', oldprice_text)
        oldnumeric_price = int(oldnumeric_price_match.group())
        print("New Price:", oldnumeric_price)

        if newnumeric_price > oldnumeric_price:
            print(f"product quantity increased to {product_quantity}")
        else:
            print("Quantity has not changed.")

        # decrease quantity
        minus_button_locator = cart_parent_element.find_element(By.CLASS_NAME, "product-qty__btn--minus")
        minus_button = self.wait.until(EC.element_to_be_clickable(minus_button_locator))

        action = ActionChains(self.driver)
        action.move_to_element(minus_button).click().perform()

        time.sleep(10)

        productqnty = cart_parent_element.find_element(By.CLASS_NAME, "product-qty__input")
        product_quantity_updated = productqnty.get_attribute("value")
        print("Updated Quantity:", product_quantity_updated)

        # Compare the updated quantity with the previous quantity
        if product_quantity_updated < product_quantity:
            print(f"Product quantity decreased to {product_quantity_updated}")
        else:
            print("Quantity has not changed.")


        # to clear entire shopping list
        self.driver.execute_script("arguments[0].scrollTo(0, 0);", cart_parent_element)

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






