import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class Access_System_Cancel:
    def __init__(self, driver, name='Daniel Pinto Martins', cpf='30562418202', phone='16889636073', email='DanielPintoMartins@jourrapide.com', password='ruo0boh9Eigh'):
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.email = email
        self.password = password
        self.driver = driver

    def add_button_product(self):
        #click button
        WebDriverWait (self.driver, 10).until (lambda s: s.find_element_by_id('click')).is_displayed()
        bnt_userCad = self.driver.find_element_by_id ('click')
        bnt_userCad.click()
        
        #name
        fieldName = self.driver.find_element_by_id ('mat-input-2')
        fieldName.send_keys(self.name)

        #cpf
        textCPF = self.driver.find_element_by_id ('mat-input-3')
        textCPF.send_keys (self.cpf)

        #phone_number
        textPhone = self.driver.find_element_by_id ('mat-input-4')
        textPhone.send_keys (self.phone)

        #email
        textEmail = self.driver.find_element_by_id ('mat-input-5')
        textEmail.send_keys (self.email)

        #passwords
        textPasswords = self.driver.find_element_by_id ('mat-input-6')
        textPasswords.send_keys (self.password)

        #repet_passwords
        textRepetPasswords = self.driver.find_element_by_id ('mat-input-7')
        textRepetPasswords.send_keys (self.password)

        #save_button
        btnSave = self.driver.find_element_by_id ('cancelbutton')
        btnSave.send_keys(Keys.RETURN)
        WebDriverWait (self.driver, 10).until (lambda s: s.find_element_by_id('click')).is_displayed()
        bnt_userCad = self.driver.find_element_by_id ('click')