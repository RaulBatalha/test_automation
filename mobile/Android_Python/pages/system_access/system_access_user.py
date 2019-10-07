from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as elementWait


class DialerLogin:
    def __init__(self, driver):
        self.driver = driver

    def button_login(self):
        #field name
        fieldName = self.driver.find_elements_by_id('userName')
        fieldName[0].clear()
        fieldName[0].send_keys('Test_Usuario')
        #field Password
        fieldPWS = self.driver.find_elements_by_id('userPassword')
        fieldPWS[0].clear()
        fieldPWS[0].send_keys('123')
        #button save
        bntSave = self.driver.find_elements_by_id('enter_app_button')
        for save in bntSave:
            if save.text == 'ENTRAR':
                save.click()