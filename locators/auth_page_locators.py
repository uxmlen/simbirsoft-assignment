from selenium.webdriver.common.by import By


class AuthPageLocators:
    # main
    BUTTON_CUSTOMER_LOGIN = (By.XPATH, '//button[@ng-click="customer()"]')
    BUTTON_MANAGER_LOGIN = (By.XPATH, '//button[@ng-click="manager()"]')

    # customer
    SELECTOR_YOUR_NAME = (By.ID, "userSelect")
    SUBMIT_BUTTON_LOGIN = (By.XPATH, '//button[@type="submit"]')
