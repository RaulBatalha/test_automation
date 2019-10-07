from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
url = 'http://172.100.10.101:7201/login'

class Access_System:
    def acess_system(self):
        self.driver = webdriver.Chrome (ChromeDriverManager().install())
        instance = self.driver.get(url)
        WebDriverWait (self.driver, 10).until (lambda s: s.find_element_by_id('mat-input-0')).is_displayed()
        textSenha = self.driver.find_element_by_id ('mat-input-0')
        textSenha.send_keys ('daniel@email.org')
        WebDriverWait (self.driver, 10).until (lambda s: s.find_element_by_id('mat-input-1')).is_displayed()
        textSenha = self.driver.find_element_by_id ('mat-input-1')
        textSenha.send_keys ('123')
        btnLogin = self.driver.find_element_by_id ('enterbutton')
        btnLogin.send_keys(Keys.RETURN)


