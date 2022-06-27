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
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions


class TestTabletPytest:
    def setup_method(self, method):
        Firefox_driver_binary = "./drivers/geckodriver"
        fire_fox_options = FireFoxOptions()
        fire_fox_options.add_argument("--width=834")
        fire_fox_options.add_argument("--height=1100")
        fire_fox_options.set_preference("general.useragent.override",
                                        "Mozilla/5.0 (iPad; CPU OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                                        "like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1")
        ser_firefox = FirefoxService(Firefox_driver_binary)
        self.driver = webdriver.Firefox(service=ser_firefox, options=fire_fox_options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_gopro(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        self.driver.find_element(By.NAME, "loginEmail").click()
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneennna123456@gmail.com")
        self.driver.find_element(By.NAME, "loginPassword").click()
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Haneen12345")
        time.sleep(5)
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".MenuMobile_preHeaderItems__IwY_9 > .GenericItemController_itemContainer__h3uI_:nth-child(4) .icon").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "#header > div.Header_mobileMenu__BBFeS.Header_menuOpen__cZfOE > div.MenuMobile_preHeaderItems__IwY_9 > div:nth-child(4) > div > ul > li:nth-child(5) > a").text == "Sign Out"

    def test_login_invalid_username(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        time.sleep(3)
        self.driver.execute_script(
            "document.querySelector('.MenuMobile_preHeaderItems__IwY_9 > div:nth-child(4) > a:nth-child(1)').scrollIntoView();")
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        self.driver.find_element(By.NAME, "loginEmail").click()
        self.driver.find_element(By.NAME, "loginEmail").send_keys("hanen1@gmail.com")
        self.driver.find_element(By.NAME, "loginPassword").click()
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Hha12345")
        time.sleep(3)
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(3)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".gpl-flash-message").text == "You've entered an incorrect email and password combination. Forgot your password?"


    def test_mandatory_fields(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        self.driver.execute_script(
            "document.querySelector('.MenuMobile_preHeaderItems__IwY_9 > div:nth-child(4) > a:nth-child(1)').scrollIntoView();")
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        time.sleep(4)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".login .btn-google > .btn-text").click()
        self.driver.find_element(By.ID, "identifierId").click()
        self.driver.find_element(By.ID, "identifierId").send_keys("awadhaneen12345@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(3)
        try:
            self.driver.execute_script(
                "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
            self.driver.find_element(By.LINK_TEXT, "Continue with Google").click()
            self.driver.find_element(By.ID, "identifierId").click()
            self.driver.find_element(By.ID, "identifierId").send_keys("awadhaneen12345@gmail.com")
            self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
            self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
        except:
            pass
        time.sleep(4)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-signup-finish.gp-login-container.container > div > div > form > div.form-input-wrapper > button').scrollIntoView();")

        create_account_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                      "body > main > div > div.app-container > div.gp-signup-finish.gp-login-container.container > div > div > form > div.form-input-wrapper > button")
        time.sleep(10)
        assert not create_account_btn.is_enabled()

    @pytest.mark.parametrize("validation", [True, True, False])
    def test_incorrect_values(self, validation):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        time.sleep(3)
        self.driver.execute_script(
            "document.querySelector('.MenuMobile_preHeaderItems__IwY_9 > div:nth-child(4) > a:nth-child(1)').scrollIntoView();")
        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu")
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".login .btn-google > .btn-text").click()
        self.driver.find_element(By.ID, "identifierId").click()
        self.driver.find_element(By.ID, "identifierId").send_keys("awadhaneen12345@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(2)
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(2)
        try:
            self.driver.execute_script(
                "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
            self.driver.find_element(By.CSS_SELECTOR, ".login .btn-google > .btn-text").click()
            time.sleep(3)
            self.driver.find_element(By.ID, "identifierId").click()
            time.sleep(3)
            self.driver.find_element(By.ID, "identifierId").send_keys("awadhaneen12345@gmail.com")
            self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            element = self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d")
            self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
            self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        except:
            pass
        time.sleep(7)
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345678")
        time.sleep(7)
        self.driver.find_element(By.NAME, "confirmPassword").click()
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("1234567")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".gp-form-row:nth-child(3) > .gp-checkbox > label").click()
        time.sleep(4)
        error_password = self.driver.find_element(By.CSS_SELECTOR, "body > main > div > div.app-container > "
                                                                   "div.gp-signup-finish.gp-login-container.container "
                                                                   "> div > div > form > div:nth-child(2) > "
                                                                   "div:nth-child(1) > div")
        error_confirm_password = self.driver.find_element(By.CSS_SELECTOR,
                                                          "body > main > div > div.app-container > "
                                                          "div.gp-signup-finish.gp-login-container.container > div > "
                                                          "div > form > div:nth-child(2) > div:nth-child(5) > div > i")
        time.sleep(2)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-signup-finish.gp-login-container.container > div > div > form > div.form-input-wrapper > button').scrollIntoView();")
        create_account_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                      "body > main > div > div.app-container > "
                                                      "div.gp-signup-finish.gp-login-container.container > div > div "
                                                      "> form > div.form-input-wrapper > button")
        errors_list = [error_password.is_displayed(), error_confirm_password.is_displayed(),
                       create_account_btn.is_enabled()]
        assert validation in errors_list

    def test_create_account(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        self.driver.execute_script(
            "document.querySelector('.MenuMobile_preHeaderItems__IwY_9 > div:nth-child(4) > a:nth-child(1)').scrollIntoView();")
        time.sleep(7)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".login .btn-google > .btn-text").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(5)
        self.driver.find_element(By.ID, "identifierId").send_keys("testerhaneen@gmail.com")
        # self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(5)
        try:
            self.driver.execute_script(
                "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
            self.driver.find_element(By.CSS_SELECTOR, ".login .btn-google > .btn-text").click()
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,0)")
            time.sleep(5)
            self.driver.find_element(By.ID, "identifierId").send_keys("testerhaneen@gmail.com")
            # self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
            self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            time.sleep(5)
            self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            time.sleep(5)
        except:
            pass
        self.driver.find_element(By.NAME, "password").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-signup-finish.gp-login-container.container > div > div > form > div:nth-child(2) > div:nth-child(5) > input').scrollIntoView();")
        self.driver.find_element(By.NAME, "confirmPassword").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("Hha12345")
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('.gp-form-row:nth-child(3) > .gp-checkbox > label').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".gp-form-row:nth-child(3) > .gp-checkbox > label").click()
        time.sleep(5)
        self.driver.switch_to.frame(0)
        self.driver.execute_script(
            "document.querySelector('.recaptcha-checkbox-border').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        time.sleep(10)
        self.driver.get("https://gopro.com/login")
        assert self.driver.current_url == "https://gopro.com/login"
        # self.driver.execute_script(
        #     "document.querySelector('body > main > div > div.app-container > div.gp-signup-finish.gp-login-container.container > div > div > form > div.form-input-wrapper > button').scrollIntoView();")
        # create_account_btn = self.driver.find_element(By.CSS_SELECTOR,
        #                                               "body > main > div > div.app-container > div.gp-signup-finish.gp-login-container.container > div > div > form > div.form-input-wrapper > button")
        # time.sleep(10)
        # assert create_account_btn.is_enabled()


    def test_search_product_gopro(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".MenuMobile_headerItems__mdiaf > .GenericItemController_itemContainer__h3uI_:nth-child(1) > .GenericItemController_accordionTitle__v0gTD > div:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .link-reset > div").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".CategoryMenu_ico__1mvB9 > .icon-product-search").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".CategoryMenu_ico__1mvB9 > .icon-product-search")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "search-box").send_keys("HERO10")
        self.driver.find_element(By.ID, "search-box").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "search-box").send_keys("HERO10")
        self.driver.find_element(By.ID, "search-box").send_keys(Keys.ENTER)
        product = self.driver.find_element(By.CSS_SELECTOR,
                                           "#__next > div:nth-child(4) > div > div.BuyModule_buyModuleWrapper__PuJLk > div > div.BuyModule_headline__XfxIu > div.Headline_headline___rce6 > h1").text

        assert product == "HERO10 Black Creator Edition"

    def test_buy_product_gorpo(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('.MenuMobile_preHeaderItems__IwY_9 > div:nth-child(4) > a:nth-child("
            "1)').scrollIntoView();")
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "loginEmail").click()
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneennna123456@gmail.com")
        self.driver.find_element(By.NAME, "loginPassword").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Haneen12345")
        time.sleep(10)
        self.driver.execute_script(
            "document.getElementById('gptest-login-btn').scrollIntoView();")
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".MenuMobile_headerItems__mdiaf > "
                                 ".GenericItemController_itemContainer__h3uI_:nth-child(1) > "
                                 ".GenericItemController_accordionTitle__v0gTD > div:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .link-reset > div").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,9)")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".button-wide:nth-child(1)").click()
        time.sleep(10)
        # self.driver.find_element(By.CSS_SELECTOR, ".button-secondary").click()
        self.driver.get("https://gopro.com/en/us/shop/cart")
        time.sleep(20)
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) .col-12 span:nth-child(3) > .fa").click()
        time.sleep(10)
        self.driver.execute_script(
            "document.querySelector('.cart_checkout_cta').scrollIntoView();")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".cart_checkout_cta").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").send_keys("Haneen")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").send_keys("Tester")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").send_keys(
            "1 Mamre Drive")
        self.driver.find_element(By.CSS_SELECTOR, ".pcadescription").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_city").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode").click()
        time.sleep(5)
        dropdown = self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode")
        dropdown.find_element(By.XPATH, "//option[. = 'California']").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").send_keys("90202")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").send_keys(
            "+1 866 277 7888")
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('.cta-submit').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".cta-submit").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".borderless").click()
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('#checkout > section:nth-child(6) > div.active.payment-options > div:nth-child(9) "
            "> button').scrollIntoView();")
        save_payment_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                    "#checkout > section:nth-child(6) > div.active.payment-options > "
                                                    "div:nth-child(9) > button")
        time.sleep(5)
        assert save_payment_btn == "SAVE AND CONTINUE"

    def test_buy_product_gopro_without_account(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".MenuMobile_headerItems__mdiaf > .GenericItemController_itemContainer__h3uI_:nth-child(1) > .GenericItemController_accordionTitle__v0gTD > div:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .link-reset > div").click()
        self.driver.execute_script("window.scrollTo(0,23.66666603088379)")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".button-wide:nth-child(1)").click()
        time.sleep(20)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(10)
        self.driver.get("https://gopro.com/en/us/shop/cart")
        # self.driver.find_element(By.CSS_SELECTOR, ".button-secondary").click()
        self.driver.get("https://gopro.com/en/us/shop/cart")
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,43)")
        time.sleep(10)
        self.driver.execute_script(
            "document.querySelector('.card:nth-child(3) .col-12 span:nth-child(3) > .fa').scrollIntoView();")
        time.sleep(15)
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) .col-12 span:nth-child(3) > .fa").click()
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('.cart_checkout_cta').scrollIntoView();")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".cart_checkout_cta").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_firstName").send_keys("Haneen")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_lastName").send_keys("Tester")
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_address1").send_keys(
            "1 Mamre Drive")
        self.driver.find_element(By.CSS_SELECTOR, ".pcadescription").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_city").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").click()
        time.sleep(12)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_postalCode").send_keys("90202")
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode").click()
        time.sleep(5)
        dropdown = self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_addressFields_states_stateCode")
        dropdown.find_element(By.XPATH, "//option[. = 'California']").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "dwfrm_shipping_shippingAddress_contactInfoFields_phone").send_keys(
            "+1 866 277 7888")
        time.sleep(10)
        self.driver.execute_script(
            "document.querySelector('.cta-submit').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".cta-submit").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,235.6666717529297)")
        time.sleep(10)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#dwfrm_shipping_shippingAddress > "
                                                                  "div.address-fields-container > "
                                                                  "div.input-wrapper.invalid > div").text
        assert error_message == "Please enter an Email"

    def test_total_price_changing_gopro(self):
        self.driver.get("https://gopro.com/en/us/")
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        self.driver.execute_script(
            "document.querySelector('.MenuMobile_preHeaderItems__IwY_9 > div:nth-child(4) > a:nth-child("
            "1)').scrollIntoView();")
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        self.driver.find_element(By.NAME, "loginEmail").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneennna123456@gmail.com")
        self.driver.find_element(By.NAME, "loginPassword").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Haneen12345")
        time.sleep(5)
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".icon-product-menu").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".MenuMobile_headerItems__mdiaf > .GenericItemController_itemContainer__h3uI_:nth-child(1) > .GenericItemController_accordionTitle__v0gTD > div:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .link-reset > div").click()
        self.driver.execute_script("window.scrollTo(0,229)")
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".button-wide:nth-child(1)").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, ".button-secondary").click()
        self.driver.get("https://gopro.com/en/us/shop/cart")
        time.sleep(7)
        current_total_price = self.driver.find_element(By.CSS_SELECTOR,
                                                       "#maincontent > div.container.cart.cart-page > "
                                                       "div.row.cart_main_wrapper > "
                                                       "div.col-12.col-lg-4.totals.cart-summary > "
                                                       "div.cart_order_summary_wrapper > "
                                                       "div.row.cart_order_summary_grandtotal > div.col-4 > p").text
        time.sleep(7)
        self.driver.execute_script("window.scrollTo(0,263)")
        self.driver.execute_script(
            "document.querySelector('.card:nth-child(3) .col-12 span:nth-child(3) > .fa').scrollIntoView();")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(3) .col-12 span:nth-child(3) > .fa").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,444)")
        str_current_total_price = current_total_price.replace(",", "")
        float_current_total_price = float(str_current_total_price[1:])
        float_total_price_changing = float_current_total_price + 499.99
        expected_total_price = f"${float_total_price_changing}"

        total_price_changing = self.driver.find_element(By.CSS_SELECTOR,
                                                        "#maincontent > div.container.cart.cart-page > "
                                                        "div.row.cart_main_wrapper > "
                                                        "div.col-12.col-lg-4.totals.cart-summary > "
                                                        "div.cart_order_summary_wrapper > "
                                                        "div.row.cart_order_summary_grandtotal > div.col-4 > p").text

        assert total_price_changing.replace(",", "") == expected_total_price
