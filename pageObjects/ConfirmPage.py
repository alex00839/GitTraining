from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    actualCountry = (By.LINK_TEXT, "India")
    confirmCountry = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "input[type='submit']")
    successText = (By.CLASS_NAME, "alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getActualCountry(self):
        return self.driver.find_element(*ConfirmPage.actualCountry)

    def getConfirmCountry(self):
        return self.driver.find_element(*ConfirmPage.confirmCountry)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)


