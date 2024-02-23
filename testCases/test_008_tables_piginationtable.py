from pageObjects.HomePage import HomePage
from pageObjects.PaginationTablePage import PaginationTablePage
from utilities.readProperties import ReadConfig
import time


class Test_PiginationTable:

    baseURL = ReadConfig.getApplicationURL()

    def test_piginationtable(self, setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickTables()
        self.hp.clickPiginationTable()

        self.ptp = PaginationTablePage(self.driver)
        self.ptp.getTableData()
        time.sleep(2)
