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


class TestBuyProductGorpoPytest:
    def setup_method(self, method):
        chrome_driver_binary = r'.\drivers\chromedriver'
        self.driver = webdriver.Chrome(chrome_driver_binary)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_buy_product_gorpo(self):
        self.driver.get("https://gopro.com/en/us/en")
        self.driver.set_window_size(1050, 660)
        self.driver.switch_to.frame(0)
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        self.driver.switch_to.default_content()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginEmail").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneennna12345@gmail.com")
        time.sleep(30)
        self.driver.find_element(By.NAME, "loginPassword").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Hha12345")
        time.sleep(20)
        # self.driver.switch_to.frame(0)
        # self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        # self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(20)
        self.driver.find_element(By.LINK_TEXT, "Cameras").click()
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "SHOP HERO10 Black").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".AddToCart_addToCart__b2V5U > .button").click()
        time.sleep(10)
        element = self.driver.find_element(By.CSS_SELECTOR, ".AddToCart_addToCart__b2V5U > .button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".button-secondary").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .col-4 span:nth-child(3) > .fa").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".cart_checkout_cta").click()
        time.sleep(10)
        shipping_info = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#checkout > section.shipping-section > div.section-header > h1")
        assert shipping_info.text == "1: Shipping Info"

    def test_buy_product_gorpo2(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.set_window_size(1292, 692)
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginEmail").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneennna12345@gmail.com")
        time.sleep(40)
        self.driver.find_element(By.NAME, "loginPassword").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Hha12345")
        # self.driver.switch_to.frame(0)
        # self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        # self.driver.switch_to.default_content()
        time.sleep(10)
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Cameras").click()
        time.sleep(10)
        element = self.driver.find_element(By.LINK_TEXT, "Cameras")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        self.driver.execute_script("window.scrollTo(0,639)")
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "SHOP HERO10 Black").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(5)
        element = self.driver.find_element(By.CSS_SELECTOR, ".VariantSelector_active__9PhY1")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".AddToCart_addToCart__b2V5U > .button").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".button-secondary").click()
        time.sleep(30)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".card:nth-child(2) .col-4 span:nth-child(3) > .fa").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".cart_checkout_cta").click()
        time.sleep(10)
        ## saved shipping details
        try:
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").send_keys(
                "Haneen")
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").send_keys("Tester")
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").send_keys(
                "1 Mamre Drive")
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_city").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_city").send_keys("Falkirk")
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode").click()
            time.sleep(5)
            dropdown = self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode")
            dropdown.find_element(By.XPATH, "//option[. = 'California']").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").send_keys(
                "90202")
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").click()
            time.sleep(5)
            self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").send_keys(
                "+1 866 277 7888")
            self.driver.find_element(By.CSS_SELECTOR, ".cta-submit").click()
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, ".borderless").click()
        except:
            pass
        time.sleep(10)
        save_payment_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                    "#checkout > section:nth-child(6) > div.active.payment-options > "
                                                    "div:nth-child(9) > button").text
        time.sleep(10)
        assert save_payment_btn == "SAVE AND CONTINUE"

    def test_buy_product_gopro_without_account(self):
        self.driver.get("https://gopro.com/en/us/en")
        self.driver.set_window_size(1050, 660)
        self.driver.switch_to.frame(0)
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Cameras").click()
        time.sleep(10)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.LINK_TEXT, "Cameras")
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "SHOP HERO10 Black").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".AddToCart_addToCart__b2V5U > .button").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".button-secondary").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .col-4 span:nth-child(3) > .fa").click()
        time.sleep(10)
        element = self.driver.find_element(By.CSS_SELECTOR, ".cart_checkout_cta")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".cart_checkout_cta").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").send_keys("Haneen")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").send_keys("Tester")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").send_keys(
            "1 Mamre Drive")
        time.sleep(20)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_city").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_city").send_keys("Falkirk")
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode").click()
        time.sleep(5)
        dropdown = self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode")
        time.sleep(5)
        dropdown.find_element(By.XPATH, "//option[. = 'California']").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").click()
        time.sleep(5)
        # actions = ActionChains(self.driver)
        # actions.double_click(element).perform()
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").send_keys("90202")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").send_keys(
            "+1 866 277 7888")
        self.driver.find_element(By.CSS_SELECTOR, ".cta-submit").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,350.3333435058594)")
        time.sleep(10)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#dwfrm_shipping_shippingAddress > "
                                                                  "div.address-fields-container > "
                                                                  "div.input-wrapper.invalid > div").text
        assert error_message == "Please enter an Email"

