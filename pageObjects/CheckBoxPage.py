from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ChexkboxPage():
    cbox_singlecheckbox_xpath = "//div//form//label//input[1]"
    txt_confmsg_xpath = "//div[@id='txtAge']"

    cbox_multiple_xpath = "//div[@class='panel-body']/div/label/input"

    btn_allcheckbox_xpath = "//input[@id='check1']"



    def __init__(self, driver):
        self.driver = driver

    def clickSingleCheckBox(self):
        box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cbox_singlecheckbox_xpath))
        )
        box.click()

    def getConfMsgofCheckBox(self):
        try:
            box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.txt_confmsg_xpath))
            )
            return box
        except:
            print("unable to find the text msg element")

    def clickMultipleCheckBoxes(self):
        box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_allcheckbox_xpath))
        )
        box.click()

    def getButtonText(self):
        try:
            box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.btn_allcheckbox_xpath))
            )
            return box.get_attribute("value")
        except:
            print("Unable to get btn element")

    
