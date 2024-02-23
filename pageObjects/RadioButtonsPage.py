from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class RadioButtonsPage:
    rbuttons_sex_xpath = "//div[@class='panel-body']/label/input"
    btn_check_xpath = "//button[@id='buttoncheck']"
    txt_message_xpath = "//p[@class='radiobutton']"


    rbuttons_sexwithgroup_xpath = "//div[@class='panel-body']/div[1]/label/input"
    rbuttons_agewithgroup_xpath = "//div[@class='panel-body']/div[2]/label/input"
    btn_getvalue_xpath = "//button[normalize-space()='Get values']"
    text_value_xpath = "//p[@class='groupradiobutton']"


    def __init__(self, driver):
        self.driver = driver

    def selectSex(self):
        count = 0
        while count < 6:
            sex = self.driver.find_elements(By.XPATH, self.rbuttons_sex_xpath)
            for item in sex:
                item.click()
                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.btn_check_xpath))
                )
                button.click()

                msg = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.txt_message_xpath))
                )
                print(msg.text)
                print("===============================")
                count += 1
        print("---------------------------------------------")


    def clickSexAndAge(self):
        count = 0
        while count < 2:
            sex = self.driver.find_elements(By.XPATH, self.rbuttons_sexwithgroup_xpath)
            for item in sex:
                item.click()
                ages = self.driver.find_elements(By.XPATH, self.rbuttons_agewithgroup_xpath)
                for age in ages:
                    age.click()
                    button = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.btn_getvalue_xpath))
                    )
                    button.click()

                    msg = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, self.text_value_xpath))
                    )
                    print(msg.text)
                    print("===================")

                    count += 1




