import os
import unittest
import subprocess
from appium import webdriver
from time import sleep

dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__),'apk/app-pedija.apk'))
 
class ChessAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Galaxy A5 (2017)'
        #desired_caps['app'] = dirPath
        desired_caps['appPackage'] = 'com.app4point.pedija'
        desired_caps['appActivity'] = '.activity.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_00_click_button_permission(self):
        button_permission = self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        sleep(10)
        self.click_button = subprocess.Popen('adb shell input tap 250 450', stdout=subprocess.PIPE).communicate()[0]
    
    #def test_01_new_user_account_registration(self):
        #self.click_button = subprocess.Popen('adb shell input tap 250 450', stdout=subprocess.PIPE).communicate()[0]
 
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)