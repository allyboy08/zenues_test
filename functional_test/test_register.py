import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        

    def test_register(self):
        driver = self.driver
        
        driver.get("https://zenues.online/")
        self.assertIn("zenues", driver.title)
        reglink = driver.find_element_by_link_text('Register')
        
        reglink.click()
        
        
        user = driver.find_element_by_xpath("(//input[@name='username'])[2]") 
        user.send_keys("testing")
        
        email = driver.find_element_by_xpath("//input[@placeholder='Email']")
        email.send_keys('zayaan@lcstudio.co.za')
            
        user_pass = driver.find_element_by_xpath("(//input[@placeholder='Password'])[2]")
        user_pass.send_keys('working123')
        
        user_pass2 = driver.find_element_by_xpath("//input[@placeholder='Repeat Password']")
        user_pass2.send_keys('working123')
            
        
        drop = driver.find_element_by_xpath("//button[@title='Select']//span")
        drop.click()
        book = driver.find_element_by_xpath("//span[text()='I want to book']")
        book.click()
        
        driver.find_element_by_xpath("//label[text()=' I agree with your ']").click() 
        
        regbtn = driver.find_element_by_xpath('//button[text()="Register"]')
        
        regbtn.click()
        
        
        time.sleep(10)
        

    def test_register_without_filling_in_fields(self):
        driver = self.driver
        
        driver.get("https://zenues.online/")
        self.assertIn("zenues", driver.title)
        reglink = driver.find_element_by_link_text('Register')
        
        reglink.click()
        
        try:
            regbtn = driver.find_element_by_xpath('//button[text()="Register"]')
            regbtn.click()
        except Exception as err:
            print(err)
            
        time.sleep(10)
    
       


# execute the script
if __name__ == "__main__":
	    unittest.main()