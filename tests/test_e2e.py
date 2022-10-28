from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#@pytest.mark.usefixtures("setup")
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()  #call next PageObject
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()

        for card in cards:
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter().click()

        checkOutPage.checkOutButton().click()

        confirmPage = checkOutPage.checkOutItems() #call next PageObject
        log.info("Entering country name as ind")
        confirmPage.getCountry().send_keys("ind")
        self.verifyLinkPresense("India")
        confirmPage.getActualCountry().click()
        confirmPage.getConfirmCountry().click()
        confirmPage.getSubmitButton().click()
        successText = confirmPage.getSuccessText().text
        log.info("Text received from application is " + successText)

        assert "Success! Thank you!" in successText