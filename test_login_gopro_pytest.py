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



class TestloginGoproPytest():
    def setup_method(self, method):
        #chrome browser:
        chrome_driver_binary = r'.\drivers\chromedriver'
        self.driver = webdriver.Chrome(chrome_driver_binary)


        #firefox browser:
        # firefox_driver_binary = "./drivers/geckodriver"
        # ser_firefox = FirefoxService(firefox_driver_binary)
        # self.driver = webdriver.Firefox(service=ser_firefox)

        # edge browser:
        # edge_driver_binary = "./drivers/msedgedriver"
        # self.driver=webdriver.Edge(edge_driver_binary)
        # dc = {
        #     "browserName": "chrome",
        #     "platformName": "WINDOWS10"
        # }
        #

        # # selenium grid standAlone
        # self.driver = webdriver.Remote("http://localhost:4444",dc)

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_gopro(self):
        self.driver.get("https://gopro.com/en/us/en")
        # self.driver.set_window_size(1050, 660)
        self.driver.switch_to.frame(0)
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.find_element(By.NAME, "loginEmail").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneenawadd12345@gmail.com")
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > form > div:nth-child(3) > input').scrollIntoView();")
        self.driver.find_element(By.NAME, "loginPassword").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Haneen12345")
        time.sleep(5)
        # self.driver.switch_to.frame(0)
        # self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        self.driver.execute_script(
            "document.getElementById('gptest-login-btn').scrollIntoView();")
        time.sleep(7)
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#header > div.Header_headerWrapper__zZm08 > "
                                 "div.Header_preHeader__JCZLg.Header_glideIn__2eE7a.Header_noShow__DK5Ts > div > div "
                                 "> div:nth-child(4) > div > div > button").click()
        time.sleep(5)
        signOut_btn = self.driver.find_element(By.CSS_SELECTOR,
                                               "#header > div.Header_headerWrapper__zZm08 > "
                                               "div.Header_preHeader__JCZLg.Header_glideIn__2eE7a"
                                               ".Header_noShow__DK5Ts > div > div > div:nth-child(4) > div > div > "
                                               "div > ul > li:nth-child(6) > a")
        assert signOut_btn.text == "Sign Out"

    def test_login_invalid_username(self):
        self.driver.get("https://gopro.com/en/us/en")
        self.driver.switch_to.frame(0)
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        time.sleep(5)
        self.driver.switch_to.default_content()
        time.sleep(7)
        self.driver.find_element(By.NAME, "loginEmail").click()
        self.driver.find_element(By.NAME, "loginEmail").send_keys("haneen1@gmail.com")
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > form > div:nth-child(3) > input').scrollIntoView();")
        self.driver.find_element(By.NAME, "loginPassword").click()
        time.sleep(7)
        self.driver.find_element(By.NAME, "loginPassword").send_keys("Hha12345")
        time.sleep(5)
        self.driver.execute_script(
            "document.getElementById('gptest-login-btn').scrollIntoView();")
        time.sleep(5)
        self.driver.find_element(By.ID, "gptest-login-btn").click()
        time.sleep(7)
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".gpl-flash-message").text
        time.sleep(5)
        assert error_message == "You've entered an incorrect email and password combination. Forgot your password?"

    def test_mandatory_fields(self):
        self.driver.get("https://gopro.com/en/us/en")
        self.driver.switch_to.frame(0)
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        # time.sleep(20)
        # self.driver.switch_to.default_content()
        time.sleep(5)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Continue with Google").click()
        time.sleep(20)
        self.driver.find_element(By.ID, "identifierId").send_keys("awadhaneen12345@gmail.com")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(7)
        self.driver.execute_script(
             "document.querySelector('body > main > div > div.app-container >div.gp-signup-finish.gp-login-container.container> div > div > form > div.form-input-wrapper > button').scrollIntoView();")
        create_account_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                      "body > main > div > div.app-container > "
                                                      "div.gp-signup-finish.gp-login-container.container > div > div "
                                                      "> form > div.form-input-wrapper > button")
        time.sleep(10)
        assert not create_account_btn.is_enabled()

    @pytest.mark.parametrize("validation", [True, True, False])
    def test_incorrect_values(self, validation):
        self.driver.get("https://gopro.com/en/us/en")
        # self.driver.set_window_size(1292, 692)
        self.driver.switch_to.frame(0)
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        time.sleep(10)
        self.driver.switch_to.default_content()

        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
        time.sleep(7)
        self.driver.find_element(By.LINK_TEXT, "Continue with Google").click()
        self.driver.find_element(By.ID, "identifierId").send_keys("awadhaneen12345@gmail.com")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(15)
        self.driver.find_element(By.NAME, "password").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "password").send_keys("12345678")
        time.sleep(10)
        self.driver.find_element(By.NAME, "confirmPassword").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("1234567")
        time.sleep(10)
        self.driver.execute_script(
             "document.querySelector('.gp-form-row:nth-child(3) > .gp-checkbox > label').scrollIntoView();")
        self.driver.find_element(By.CSS_SELECTOR, ".gp-form-row:nth-child(3) > .gp-checkbox > label").click()
        time.sleep(10)
        self.driver.switch_to.frame(0)
        # self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        error_password = self.driver.find_element(By.CSS_SELECTOR, "body > main > div > div.app-container > "
                                                                   "div.gp-signup-finish.gp-login-container.container "
                                                                   "> div > div > form > div:nth-child(2) > "
                                                                   "div:nth-child(1) > div")
        error_confirm_password = self.driver.find_element(By.CSS_SELECTOR,
                                                          "body > main > div > div.app-container > "
                                                          "div.gp-signup-finish.gp-login-container.container > div > "
                                                          "div > form > div:nth-child(2) > div:nth-child(5) > div > i")


        create_account_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                      "body > main > div > div.app-container > "
                                                      "div.gp-signup-finish.gp-login-container.container > div > div "
                                                      "> form > div.form-input-wrapper > button")
        errors_list = [error_password.is_displayed(), error_confirm_password.is_displayed(),
                       create_account_btn.is_enabled()]
        assert validation in errors_list

    def test_create_account(self):
        self.driver.get("https://gopro.com/en/us/")
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        time.sleep(10)
        self.driver.execute_script(
            "document.querySelector('body > main > div > div.app-container > div.gp-slider > div > div:nth-child(1) > div > div > div > div:nth-child(4) > div > div.social.login.ecomm-subscriber > p:nth-child(3) > a').scrollIntoView();")
        time.sleep(7)
        self.driver.find_element(By.CSS_SELECTOR, ".login .btn-google > .btn-text").click()
        time.sleep(10)
        # self.driver.find_element(By.CSS_SELECTOR, ".eARute > .lCoei").click()
        # time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(10)
        self.driver.find_element(By.ID, "identifierId").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "identifierId").click()
        time.sleep(10)
        element = self.driver.find_element(By.ID, "identifierId")
        time.sleep(10)
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "identifierId").click()
        time.sleep(10)
        self.driver.find_element(By.ID, "identifierId").send_keys("testerhaneen@gmail.com")
        time.sleep(20)
        self.driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button").click()
        time.sleep(10)
        # self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
        # time.sleep(10)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
        time.sleep(15)
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".gpl-icon-close").click()
            time.sleep(10)
            self.driver.find_element(By.LINK_TEXT, "Continue with Google").click()
            time.sleep(10)
            self.driver.find_element(By.CSS_SELECTOR, ".eARute > .lCoei").click()
            time.sleep(10)
            self.driver.execute_script("window.scrollTo(0,0)")
            self.driver.find_element(By.ID, "identifierId").click()
            time.sleep(10)
            self.driver.find_element(By.ID, "identifierId").click()
            time.sleep(10)
            element = self.driver.find_element(By.ID, "identifierId")
            time.sleep(10)
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            self.driver.find_element(By.ID, "identifierId").click()
            time.sleep(10)
            self.driver.find_element(By.ID, "identifierId").send_keys("testerhaneen@gmail.com")
            time.sleep(10)
            # self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            self.driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button").click()
            time.sleep(10)
            self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
            # self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-RLmnJb").click()
            self.driver.find_element(By.CSS_SELECTOR, ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > .VfPpkd-vQzf8d").click()
            time.sleep(15)
        except:
            pass
        self.driver.find_element(By.NAME, "password").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "password").send_keys("Hha12345")
        self.driver.find_element(By.NAME, "confirmPassword").click()
        time.sleep(10)
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("Hha12345")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".gp-form-row:nth-child(3) > .gp-checkbox > label").click()
        try:
            self.driver.switch_to.frame(0)
            self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
        except:
            pass
        time.sleep(20)

        self.driver.get("https://gopro.com/login")
        assert self.driver.current_url=="https://gopro.com/login"
        # create_account_btn= self.driver.find_element(By.CSS_SELECTOR,"body > main > div > div.app-container > div.gp-signup-finish.gp-login-container.container > div > div > form > div.form-input-wrapper > button")
        # time.sleep(20)
        # assert create_account_btn.is_enabled()
