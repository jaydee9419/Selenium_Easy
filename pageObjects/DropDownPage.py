from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class DropDownPage:
    lst_singlelist_xpath = "//select[@id='select-demo']"
    txt_singlelistselected_xpath = "//p[@class='selected-value']"

    lst_multiplelist_xpath = "//select[@name='States']"
    btn_firstselected_xpath = "//button[@id='printMe']"
    btn_getallselected_xpath = "//button[@id='printAll']"
    txt_multiplelistselected_xpath = "//p[@class='getall-selected']"

    def __init__(self, driver):
        self.driver = driver

    def selectMonday(self):
        days = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_singlelist_xpath))
        )
        drop_days = Select(days)
        drop_days.select_by_visible_text("Monday")

    def selectTuesday(self):
        days = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_singlelist_xpath))
        )
        drop_days = Select(days)
        drop_days.select_by_index(3)

    def selectWednesday(self):
        days = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_singlelist_xpath))
        )
        drop_days = Select(days)
        drop_days.select_by_value("Wednesday")

    def selectThursday(self):
        days = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_singlelist_xpath))
        )
        drop_days = Select(days)
        drop_days.select_by_visible_text("Thursday")

    def selectFriday(self):
        days = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_singlelist_xpath))
        )
        drop_days = Select(days)
        drop_days.select_by_visible_text("Friday")

    def selectSaturday(self):
        days = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_singlelist_xpath))
        )
        drop_days = Select(days)
        drop_days.select_by_visible_text("Saturday")

    def selectSunday(self):
        days = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_singlelist_xpath))
        )
        drop_days = Select(days)
        drop_days.select_by_visible_text("Sunday")

    def getSelectedDayInfo(self):
        msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txt_singlelistselected_xpath))
        )
        print(msg.text)

# 2nd method

    def clickFirstState(self):
        first = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_firstselected_xpath))
        )
        first.click()

    def seletMultipleStates(self):
        multiple = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.lst_multiplelist_xpath))
        )
        select_multiple = Select(multiple)
        select_multiple.select_by_value("California")
        select_multiple.select_by_value("New Jersey")
        select_multiple.select_by_value("New York")

    def clickMultipleStates(self):
        multiple = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_getallselected_xpath))
        )
        multiple.click()

    def getSelectedStatesInfo(self):
        msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.txt_multiplelistselected_xpath))
        )
        print(msg.text)


