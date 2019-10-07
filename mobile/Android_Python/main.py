import os, unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
######################### pages ##############################
from androidriver.androidriver import DriverAndroid
from pages.system_access.system_access_user import DialerLogin
from pages.read_qrcode.read_qrcode import Dialer_Read_QrCode

class DialerTestCases(unittest.TestCase, DriverAndroid):
    def setUp(self):
        DriverAndroid.__init__ (self)
    
    def tearDown(self):
        self.driver.quit ()

    #def test_00_user_login(self):
    #    login = DialerLogin(self.driver).button_login()
    #    self.assertEqual('Test_Usuario', 'Test_Usuario')
    #    self.assertEqual('123', '123')
    
    def test_01_click_qrcode (self):
        login = DialerLogin(self.driver).button_login()
        qrcode = Dialer_Read_QrCode(self.driver).read_qrcode()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DialerTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)