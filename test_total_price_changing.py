import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTotalPriceChangingPytest():
    def setup_method(self, method):
        chrome_driver_binary = r'.\drivers\chromedriver'
        self.driver = webdriver.Chrome(chrome_driver_binary)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_total_price_changing_gopro(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.set_window_size(1292, 692)
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginEmail").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneennna12345@gmail.com")
        time.sleep(30)
        self.driver.find_element(By.NAME, "loginPassword").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Hha12345")
        time.sleep(20)
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Cameras").click()
        time.sleep(10)
        element = self.driver.find_element(By.LINK_TEXT, "SHOP HERO9 Black")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "SHOP HERO9 Black").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".AddToCart_addToCart__b2V5U > .button").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".button-secondary").click()
        time.sleep(5)
        current_total_price = self.driver.find_element(By.CSS_SELECTOR,
                                                       "#maincontent > div.container.cart.cart-page > "
                                                       "div.row.cart_main_wrapper > "
                                                       "div.col-12.col-lg-4.totals.cart-summary > "
                                                       "div.cart_order_summary_wrapper > "
                                                       "div.row.cart_order_summary_grandtotal > div.col-4 > p").text
        time.sleep(7)
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .col-4 span:nth-child(3) > .fa").click()
        time.sleep(10)
        str_current_total_price = current_total_price.replace(",","")
        float_current_total_price = float(str_current_total_price[1:])
        float_total_price_changing = float_current_total_price + 399.99
        expected_total_price = f"${float_total_price_changing}"

        total_price_changing = self.driver.find_element(By.CSS_SELECTOR,
                                                        "#maincontent > div.container.cart.cart-page > div.row.cart_main_wrapper > div.col-12.col-lg-4.totals.cart-summary > div.cart_order_summary_wrapper > div.row.cart_order_summary_grandtotal > div.col-4 > p").text

        assert total_price_changing.replace(",","")==expected_total_price