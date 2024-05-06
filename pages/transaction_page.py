import csv

import allure
from allure import attachment_type

from locators.transaction_page_locators import TransactionsPageLocators

from .base_page import BasePage


class TransactionPage(BasePage):
    locators = TransactionsPageLocators()

    @property
    @allure.step("Get all transactions")
    def get_all_transactions(self):
        self.element_is_visible(self.locators.BUTTON_TRANSACTIONS).click()
        return self.elements_are_visible(self.locators.TRANSACTION_ROWS)

    @allure.step("Generate CSV report")
    def generate_report_csv(self, transactions):
        path = "transactions.csv"
        with open(path, "w", newline="", encoding="utf-8") as f:
            write = csv.writer(f)
            write.writerow(["Data-Time", "Amount", "Transaction Type"])
            for transaction in transactions:
                write.writerow(
                    d.text
                    for d in transaction.find_elements(*self.locators.TRANSACTION_TD)
                )

        allure.attach.file(
            path, name="Transactions Report", attachment_type=attachment_type.CSV
        )
