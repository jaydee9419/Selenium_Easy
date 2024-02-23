from pageObjects.HomePage import HomePage
from pageObjects.BoostarpDatePickerPage import BoostrapDatePickerPage
from utilities.readProperties import ReadConfig


class Test_Bootstrap:

    baseURL = ReadConfig.getApplicationURL()

    def test_bootstrap(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickDatePicker()
        self.hp.clickBootstrapDatePicker()

        self.bsdp = BoostrapDatePickerPage(self.driver)
        self.bsdp.clickCalender()
        self.bsdp.clickToday()
        date = self.bsdp.getDateInfo()
        print(date)
        self.bsdp.clickCalender()
        self.bsdp.clearDate()
        date = self.bsdp.getDateInfo()
        print(date)

        self.bsdp.setStartDate()
        date = self.bsdp.getStartDate()
        print(date)
        date = self.bsdp.getEndDate()
        print(date)

