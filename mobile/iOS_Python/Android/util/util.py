import subprocess
import time
import os
import uiautomator2 as devices

dt = time.time()
deviceConnect = devices.connect ('192.168.137.191:5555')

class TestAndroid (self):
    def setUp(self):
      self.startActivity = subprocess.Popen.stdout ("adb shell am start -a android.intent.action.MAIN -n com.app4point.pedija/.activity.MainActivity", stdout=subprocess.PIPE).comunicate()[0]
      os.self.startActivity()
      
      #self.click_button = subprocess.Popen('adb shell input tap 250 450', stdout=subprocess.PIPE).communicate()[0]

if __name__=='__main__':
    a = TestAndroid()
    a.setUp()