from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage():
    # input form manu
    lnk_inputformsmenu_link = 'Input Forms'
    txt_simpleformdemo_xpath = "//ul[@class='dropdown-menu']//a[normalize-space()='Simple Form Demo']"
    txt_ckeckbox_xpath = "//ul[@class='dropdown-menu']//a[normalize-space()='Checkbox Demo']"
    txt_radiobutton_link = "Radio Buttons Demo"
    txt_dropdown_xpath = "//ul[@class='dropdown-menu']//a[normalize-space()='Select Dropdown List']"
    txt_ajxformsubmit_xpath = "//ul[@class='dropdown-menu']//a[normalize-space()='Ajax Form Submit']"

    # Date Picker
    lnk_datepicker_link = "Date pickers"
    txt_bootstrapdatepicket_xpath = "//ul[@class='dropdown-menu']//a[normalize-space()='Bootstrap Date Picker']"
    txt_jsquerydatepicker_xpath = "//ul[@class='dropdown-menu']//a[normalize-space()='JQuery Date Picker']"

    # Tables
    lnk_tables_link = "Table"
    txt_piginationtable_xpath = "//ul[@class='dropdown-menu']//a[normalize-space()='Table Pagination']"


    def __init__(self, driver):
        self.driver = driver

    def clickInputForms(self):
        input_form_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.lnk_inputformsmenu_link))
        )
        input_form_element.click()

    def clickSimpleFormDemo(self):
        simple_form_demo_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_simpleformdemo_xpath))
        )
        simple_form_demo_element.click()

    def clickCheckBox(self):
        simple_form_demo_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_ckeckbox_xpath))
        )
        simple_form_demo_element.click()


    def clickRadioButton(self):
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.txt_radiobutton_link))
        )
        radio_button.click()

    def clickDropDown(self):
        radio_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_dropdown_xpath))
        )
        radio_button.click()

    def clickAjxFormSubmit(self):
        ajaxform = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_ajxformsubmit_xpath))
        )
        ajaxform.click()

    def clickDatePicker(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.lnk_datepicker_link))
        )
        date.click()

    def clickBootstrapDatePicker(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_bootstrapdatepicket_xpath))
        )
        date.click()

    def clickJSQueryDatePicker(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_jsquerydatepicker_xpath))
        )
        date.click()


    def clickTables(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.lnk_tables_link))
        )
        date.click()

    def clickPiginationTable(self):
        date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_piginationtable_xpath))
        )
        date.click()



