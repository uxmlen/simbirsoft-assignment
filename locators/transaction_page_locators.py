from selenium.webdriver.common.by import By


class TransactionsPageLocators:
    BUTTON_TRANSACTIONS = (By.XPATH, '//button[@ng-click="transactions()"]')
    TRANSACTION_ROWS = (By.CSS_SELECTOR, "tbody tr")
    TRANSACTION_TD = (By.CSS_SELECTOR, "td[class=ng-binding]")
