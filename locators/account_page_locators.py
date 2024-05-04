from selenium.webdriver.common.by import By


class AccountPageLocators:
    BUTTON_DEPOSIT = (By.XPATH, '//button[@ng-click="deposit()"]')
    BUTTON_WITHDRAWL = (By.XPATH, '//button[@ng-click="withdrawl()"]')

    # active menu
    BUTTON_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    INPUT_AMOUNT = (By.CSS_SELECTOR, "input.form-control")

    # account info
    ACCOUNT_NUMBER = (By.CSS_SELECTOR, "strong.ng-binding:nth-child(1)")
    BALANCE = (By.CSS_SELECTOR, "strong.ng-binding:nth-child(2)")
    CURRENCY = (By.CSS_SELECTOR, "strong.ng-binding:nth-child(2)")
