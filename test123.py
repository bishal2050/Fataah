import time
import unittest

from selenium import webdriver
class MyTestCase(unittest.TestCase):

    def setUp(self):
        path = 'C:\Selenium\chromedriver_win32\chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()


    def test1login(self):
        self.driver.find_element_by_id("login2").click()
        #time.sleep(5)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("loginusername").send_keys("testmorning")
        self.driver.find_element_by_id("loginpassword").send_keys("test123")
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        time.sleep(5)
        result = "Welcome testmorning"
        time.sleep(10)
        value = self.driver.find_element_by_id("nameofuser").text

        self.assertEqual(result,value,"Does not match")


    def testcontact(self):
        contact = self.driver.find_element_by_xpath("//*[@class='navbar-collapse']/ul/li[2]/a")
        contact.click()
        time.sleep(5)
        self.driver.find_element_by_id("recipient-email").send_keys("Test1")
        self.driver.find_element_by_id("recipient-name").send_keys("Test Name")
        self.driver.find_element_by_id("message-text").send_keys("Message 1")
        self.driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[3]/button[2]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/button/span").click()
        # driver.find_element_by_id("recipient-email").send_keys("Test1")
        # driver.find_element(By.ID,"recipient-email").send_keys("BY New one")
        time.sleep(5)
        self.driver.switch_to.alert.accept()





    def tearDown(self) -> None:
        self.driver.quit();


if __name__ == '__main__':
    unittest.main()
