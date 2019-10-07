from selenium.webdriver.support.wait import WebDriverWait

class Dialer_Read_QrCode:
    def __init__(self, driver):
        self.driver = driver

    def read_qrcode(self):
        #try:
        btnQrCode = self.driver.find_element_by_accessibility_id('qrcode_button')
        for bntEnter in btnQrCode:
            if bntEnter.text == 'FAZER LEITURA':
                bntEnter.click()
        
        #except OSError:
        #    self.permissionAndroid = ('adb shell pm grant com.itbam.vane permission')
        #    self.permissionAndroid = ('adb shell pm grant com.itbam.vane android.permission.CAMERA')
