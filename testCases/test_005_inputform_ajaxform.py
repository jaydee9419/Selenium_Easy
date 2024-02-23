from pageObjects.HomePage import HomePage
from pageObjects.AjaxFormPage import AjaxFormPage
from utilities.readProperties import ReadConfig
import os
import time


class Test_AjaxForm:

    baseURL = ReadConfig.getApplicationURL()

    def test_ajexform(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickInputForms()
        self.hp.clickAjxFormSubmit()

        self.ajp = AjaxFormPage(self.driver)
        self.ajp.setName()
        self.ajp.setComment()
        self.ajp.clickSubmit()
        time.sleep(2)

        msg = self.ajp.getConfMsg()
        if msg == "Form submited Successfully!":
            print(msg)
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//AjaxForm.png")
            assert False

        self.driver.quit()

