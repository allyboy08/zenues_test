import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class TestLoginHost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
        
    def test_login_as_host_confirm_booking(self):
        driver = self.driver
        
        driver.get("https://zenues.online/")
        self.assertIn("zenues", driver.title)
        loglink = driver.find_element_by_link_text('Login')
        
        loglink.click()
        
        user = driver.find_element_by_xpath("//input[@placeholder='Username or Email']") 
        user.send_keys("Test")
        
        user_pass = driver.find_element_by_xpath("//input[@placeholder='Password']")
        user_pass.send_keys('123')
        
        logbtn = driver.find_element_by_xpath('//button[text()="Log In"]')
        
        logbtn.click()
            
        time.sleep(10)
    
       


# execute the script
if __name__ == "__main__":
	    unittest.main()