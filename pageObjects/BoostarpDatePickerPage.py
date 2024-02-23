from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BoostrapDatePickerPage:

    # Bootstrap date picker
    input_calender_xpath = "//div[@class='input-group date']//span[@class='input-group-addon']"
    btn_today_xpath = "//div[@class='datepicker-days']//th[@class='today'][normalize-space()='Today']"
    txt_date_xpath = "//input[@placeholder='dd/mm/yyyy']"
    btn_clear_xpath = "//div[@class='datepicker-days']//th[@class='clear'][normalize-space()='Clear']"

    input_start_xpath = "//input[@placeholder='Start date']"
    input_end_xpath = "//input[@placeholder='End date']"
    btn_empty_xpath = "//body/div[@class='container-fluid text-center']/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickCalender(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_calender_xpath))
        )
        date.click()

    def clickToday(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_today_xpath))
        )
        date.click()

    def getDateInfo(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txt_date_xpath))
        )
        return date.get_attribute("value")

    def clearDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_clear_xpath))
        )
        date.click()

    def setStartDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_start_xpath))
        )
        date.send_keys("22/05/1992")

    def getStartDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_start_xpath))
        )
        return date.get_attribute("value")

    def getEndDate(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_end_xpath))
        )
        return date.get_attribute("value")




