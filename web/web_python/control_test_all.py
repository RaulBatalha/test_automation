url = 'http://172.100.10.101:7201/login'
import unittest
import chromedriver_binary

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.system_access.create_new_user_cancel import Access_System_Cancel


class CmsTouchpag (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome (ChromeDriverManager().install())
        self.driver.get(url)

    #def test_00_access_system (self):
    #    self.login = Login_Valid (self.driver)
    #    self.login.date_user()

    #def test_01_access_system (self):
    #    self.login = Login_Invalid (self.driver)
    #    self.login.date_user()

    #def test_02_create_user_new_save(self):
    #    self.create_user = Access_System_Save(self.driver)
    #    self.create_user.add_button_product()
    
    def test_03_create_new_user_cancel(self):
        self.create_user = Access_System_Cancel(self.driver)
        self.create_user.add_button_product()
        self.assertEqual ('http://172.100.10.101:7201/new-admin', 'http://172.100.10.101:7201/login','Ola' )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CmsTouchpag)
    unittest.TextTestRunner(verbosity=2).run(suite)