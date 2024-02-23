from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaginationTablePage:

    tbl_tablerows_xpath = "//tbody/tr"
    tbl_tabledata_xpath = "//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    # def getTableData(self):
    #     rows = len(self.driver.find_elements(By.XPATH, self.tbl_tablerows_xpath))
    #     columns = len(self.driver.find_elements(By.XPATH, self.tbl_tabledata_xpath))
    #     for row in range(0, rows+1):
    #         for column in range(0, columns + 1):
    #             data = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(row) + "]/td[" + str(column) + "]")
    #             print(data.text, end="       ")

    # def getTableData(self):
    #     rows = len(self.driver.find_elements(By.XPATH, self.tbl_tablerows_xpath))
    #     columns = len(self.driver.find_elements(By.XPATH, self.tbl_tabledata_xpath))
    #
    #     for row in range(rows):
    #         for column in range(columns):
    #             data = self.driver.find_element(By.XPATH, f"//tbody/tr[{row + 1}]/td[{column + 1}]")
    #             print(f"{data.text}\t", end="")
    #         print()

    def getTableData(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.tbl_tablerows_xpath))
            )

            rows = self.driver.find_elements(By.XPATH, self.tbl_tablerows_xpath)

            for row in range(len(rows)):
                data = self.driver.find_elements(By.XPATH, f"{self.tbl_tablerows_xpath}[{row + 1}]/td")
                for column in range(len(data)):
                    print(f"{data[column].text}\t", end="")
                print()  # Move to the next line after printing a row

        except TimeoutException:
            print("Timed out waiting for table data to load.")



