from pageObjects.HomePage import HomePage
from pageObjects.DropDownPage import DropDownPage
from utilities.readProperties import ReadConfig
import time


class Test_DropDown:

    baseURL = ReadConfig.getApplicationURL()

    def test_dropdown(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickInputForms()
        self.hp.clickDropDown()

        self.ddp = DropDownPage(self.driver)
        self.ddp.selectMonday()
        self.ddp.getSelectedDayInfo()
        self.ddp.selectTuesday()
        self.ddp.getSelectedDayInfo()
        self.ddp.selectWednesday()
        self.ddp.getSelectedDayInfo()
        self.ddp.selectThursday()
        self.ddp.getSelectedDayInfo()
        self.ddp.selectFriday()
        self.ddp.getSelectedDayInfo()
        self.ddp.selectSaturday()
        self.ddp.getSelectedDayInfo()
        self.ddp.selectSunday()
        self.ddp.getSelectedDayInfo()

        time.sleep(2)
        self.ddp.seletMultipleStates()
        self.ddp.clickMultipleStates()
        self.ddp.getSelectedStatesInfo()
        self.ddp.clickFirstState()
        self.ddp.getSelectedStatesInfo()

        self.driver.quit()
