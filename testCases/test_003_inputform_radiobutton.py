from pageObjects.HomePage import HomePage
from pageObjects.RadioButtonsPage import RadioButtonsPage
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
        self.hp.clickRadioButton()

        self.rbp = RadioButtonsPage(self.driver)
        self.rbp.selectSex()

        self.rbp.clickSexAndAge()

