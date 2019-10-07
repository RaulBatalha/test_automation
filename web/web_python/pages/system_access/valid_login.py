from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class Valid_Login:
        def __init__ (self, driver, email='daniel@email.org', password='123'):
                self.email = email
                self.password = password
                self.driver = driver

        def user_data (self):
                WebDriverWait (self.driver, 10).until (lambda s: s.find_element_by_id('mat-input-0')).is_displayed()
                textSenha = self.driver.find_element_by_id ('mat-input-0')
                textSenha.send_keys (self.email)
                WebDriverWait (self.driver, 10).until (lambda s: s.find_element_by_id('mat-input-1')).is_displayed()
                textSenha = self.driver.find_element_by_id ('mat-input-1')
                textSenha.send_keys (self.password)
                btnLogin = self.driver.find_element_by_id ('enterbutton')
                btnLogin.send_keys(Keys.RETURN)