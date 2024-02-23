from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SimpleFormPage():

    input_usermsg_xpath = "//input[@id='user-message']"
    btn_showmsg_xpath = "//button[normalize-space()='Show Message']"
    output_usermsg_xpath = "//span[@id='display']"

    input_value1_xpath = "//input[@id='value1']"
    input_value2_xpath = "//input[@id='value2']"
    btn_gettotal_xpath = "//button[normalize-space()='Get Total']"
    output_total_xpath = "//span[@id='displayvalue']"


    def __init__(self, driver):
        self.driver = driver

    def setUserMsg(self):
        user_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_usermsg_xpath))
        )
        user_msg.send_keys("QA Automation Practice")

    def clickShowMsg(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_showmsg_xpath))
        )
        button.click()

    def getUserMsg(self):
        try:
            user_msg = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.output_usermsg_xpath))
            )
            return user_msg
        except:
            print("unable to find the output text element")

    def setValue1(self, value1):
        value_1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_value1_xpath))
        )
        value_1.send_keys(value1)

    def setValue2(self, value2):
        value_2 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.input_value2_xpath))
        )
        value_2.send_keys(value2)

    def clickTotalButton(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.btn_gettotal_xpath))
        )
        button.click()

    def getTotalValue(self):
        try:
            total = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.output_total_xpath))
            )
            return total
        except:
            print("unable to find the output text element")
