from pageObjects.HomePage import HomePage
from pageObjects.SimpleFormPage import SimpleFormPage
from utilities.readProperties import ReadConfig
import os



class Test_SimpleForms():

    baseURL = ReadConfig.getApplicationURL()

    def test_simpleforms(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickInputForms()
        self.hp.clickSimpleFormDemo()

        self.sfdp = SimpleFormPage(self.driver)
        self.sfdp.setUserMsg()
        self.sfdp.clickShowMsg()

        msg = self.sfdp.getUserMsg()
        if msg.text == "QA Automation Practice":
            print(msg.text)
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\simpleform1.png")
            assert False

        self.sfdp.setValue1("5")
        self.sfdp.setValue2("4")
        self.sfdp.clickTotalButton()

        msg = self.sfdp.getTotalValue()
        if msg.text == "9":
            print(f"given inputs are purly numerical values: {msg.text}")
            assert True
        elif msg.text == "NaN":
            print(f"given inputs are not numerical values: {msg.text}")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\simpleform2.png")
            assert False

        self.driver.quit()
