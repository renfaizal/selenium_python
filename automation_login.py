import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 

        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element_by_id("email").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        driver.find_element_by_id("password").send_keys("testerjago") # isi password
        time.sleep(1)
        driver.find_element_by_id("signin_login").click()
        time.sleep(1)

        response_data = driver.find_element_by_id("swal2-title").text
        response_message = driver.find_element_by_id("swal2-content").text

        self.assertEqual(response_data, 'Welcome tester jago')
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test_b_failed_login_with_empty_email(self):
        print ("tulis disini test case mu")

    def test_c_failed_login_with_empty_email(self):
        print ("tulis disini test case mu")

    def test_d_failed_login_with_empty_email(self):
        print ("tulis disini test case mu")

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()