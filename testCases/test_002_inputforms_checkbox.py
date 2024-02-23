from pageObjects.HomePage import HomePage
from pageObjects.CheckBoxPage import ChexkboxPage
from utilities.readProperties import ReadConfig
import time



class Test_SimpleForms():

    baseURL = ReadConfig.getApplicationURL()

    def test_simpleforms(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickInputForms()
        self.hp.clickCheckBox()

        self.cbp = ChexkboxPage(self.driver)
        self.cbp.clickSingleCheckBox()
        msg = self.cbp.getConfMsgofCheckBox()
        print(msg)
        time.sleep(2)

        msg = self.cbp.getButtonText()
        print(msg)
        time.sleep(2)
        self.cbp.clickMultipleCheckBoxes()
        msg = self.cbp.getButtonText()
        print(msg)
        time.sleep(2)

        self.cbp.clickMultipleCheckBoxes()
        time.sleep(2)
        msg = self.cbp.getButtonText()
        print(msg)
        time.sleep(2)
        self.driver.quit()
