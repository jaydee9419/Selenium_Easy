from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AjaxFormPage:
    input_name_xpath = "//input[@id='title']"
    input_comment_xpath = "//textarea[@id='description']"
    btn_sibmit_xpath = "//input[@id='btn-submit']"
    text_message_xpath = "//div[@id='submit-control']"

    def __init__(self, driver):
        self.driver = driver

    def setName(self):
        name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.input_name_xpath))
        )
        name.send_keys("Dileep")

    def setComment(self):
        comment = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.input_comment_xpath))
        )
        comment.send_keys("Hello World!.")

    def clickSubmit(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.btn_sibmit_xpath))
        )
        button.click()

    def getConfMsg(self):
        msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.text_message_xpath))
        )
        return msg.text
