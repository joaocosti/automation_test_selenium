import time
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, locator):
        elements = self.driver.find_elements( by, locator)
        while len(elements) > 0:
            elements = self.driver.find_elements( by, locator)
            time.sleep(1)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)
