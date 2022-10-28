from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.XPATH, "div/button")
    checkOutBlue = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def checkOutButton(self):
        return self.driver.find_element(*CheckoutPage.checkOutBlue)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage