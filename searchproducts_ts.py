import unittest
from selenium import webdriver
import os




class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        SAUCE_USERNAME = os.environ['SAUCE_USERNAME']
        SAUCE_ACCESS_KEY = os.environ['SAUCE_ACCESS_KEY']

        caps = {'browserName': "internet explorer"}
        caps['platform'] = "Windows 7"
        caps['version'] = "11.0"
        cls.driver = webdriver.Remote(desired_capabilities=caps,
                                       command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' %(SAUCE_USERNAME, SAUCE_ACCESS_KEY))

        cls.driver.get('http://demo-store.seleniumacademy.com/')


    # get the search textbox
    def test_search_by_cat(self):
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

    # enter search keyword and submit
        self.search_field.send_keys('phones')
        self.search_field.submit()

    # get all the anchor elements which have product names displayed
    # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(3, len(products))

    def test_search_by_name(self):
        #get search box
        self.search_field = self.driver.find_element_by_name('q')
        self.search_field.clear()

        self.search_field.send_keys("salt shaker")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))

    # close the browser window
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)