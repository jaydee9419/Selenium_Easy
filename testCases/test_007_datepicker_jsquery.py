from pageObjects.HomePage import HomePage
from pageObjects.JSQueryDAtePickerPage import JSQueryDatePickerPage
from utilities.readProperties import ReadConfig
import time


class Test_JSQuary:

    baseURL = ReadConfig.getApplicationURL()

    def test_bootstrap(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDatePicker()
        self.hp.clickJSQueryDatePicker()

        self.jqdp = JSQueryDatePickerPage(self.driver)
        self.jqdp.setFromDate()
        self.jqdp.setToDate()

        from_date = self.jqdp.getFromDate()
        print(from_date)
        to_date = self.jqdp.getToDate()
        print(to_date)

