from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class JSQueryDatePickerPage:

    # JSQuery date picker
    input_fromdate_xpath = "//input[@id='from']"
    input_todate_xpath = "//input[@id='to']"


    def __init__(self, driver):
        self.driver = driver

    def setFromDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_fromdate_xpath))
        )
        date.send_keys("22/05/1992")


    def setToDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_todate_xpath))
        )
        date.send_keys("23/02/2024")


    def getFromDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_fromdate_xpath))
        )
        return date.get_attribute("value")


    def getToDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_todate_xpath))
        )
        return date.get_attribute("value")
