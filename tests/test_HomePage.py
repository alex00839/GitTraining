import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)

        self.driver.refresh()

#    @pytest.fixture(params=[("Rahul", "Shetty", "Male"),("Anshika", "Shetty", "Female")])
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param


    print("Hello_0")
    print("Hello_1")
    print("Hello_2")
    # gjhasdakshd;l
    # kasjhkash
    # kscha;'o'aspdioua,s
    print("Hello_3")
    print("Hello_4")
    print("Hello_5")

    print("Hello_13 Develop")
    print("Hello_14 Develop")
    print("Hello_15 Develop")

    print("Hello_13 Develop America")
    print("Hello_14 Develop America")
    print("Hello_15 Develop America")