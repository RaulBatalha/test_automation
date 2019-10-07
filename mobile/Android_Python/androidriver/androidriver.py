#dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__),'apk/vane-control-v1.apk'))
import os
from appium import webdriver

class DriverAndroid:
    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'Galaxy A5 (2017)'
        #desired_caps['app'] = dirPath
        desired_caps['appPackage'] = 'com.itbam.vane'
        desired_caps['appActivity'] = 'com.itbam.vane.view.LoginActivity'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)