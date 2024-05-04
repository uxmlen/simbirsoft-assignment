import allure

from locators.account_page_locators import AccountPageLocators

from .base_page import BasePage


class AccountPage(BasePage):
    locators = AccountPageLocators()

    @allure.step("Deposit")
    def deposit(self, amount: int):
        self.element_is_visible(self.locators.BUTTON_DEPOSIT).click()
        self.element_is_visible(self.locators.INPUT_AMOUNT).send_keys(str(amount))
        self.element_is_visible(self.locators.BUTTON_SUBMIT).click()

    @allure.step("Withdraw")
    def withdraw(self, amount: int):
        self.element_is_visible(self.locators.BUTTON_WITHDRAWL).click()
        self.element_is_visible(self.locators.INPUT_AMOUNT).send_keys(str(amount))
        self.element_is_visible(self.locators.BUTTON_SUBMIT).click()

    @allure.step("Get Current Balance")
    def get_current_balance(self) -> int:
        return int(self.element_is_visible(self.locators.BALANCE).text)
