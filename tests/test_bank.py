from datetime import datetime

import allure

from config import BASE_URL
from pages.account_page import AccountPage
from pages.auth_page import AuthPage
from pages.transaction_page import TransactionPage
from utils.fib import fib


@allure.feature("Banking")
@allure.story("Transaction Complete")
@allure.severity(allure.severity_level.CRITICAL)
def test_customer_login(browser):
    auth_page = AuthPage(browser, BASE_URL)
    auth_page.open()
    auth_page.login_as_customer("Harry Potter")

    account_page = AccountPage(browser, f"{BASE_URL}/#/account")
    current_day = datetime.now().day + 1
    amount = fib(current_day)
    account_page.deposit(amount)
    account_page.withdraw(amount)

    balance = account_page.balance
    with allure.step("Check balance"):
        assert balance == 0

    transaction_page = TransactionPage(browser, f"{BASE_URL}/#/listTx")
    transactions = transaction_page.get_all_transactions

    with allure.step("Check amount of the transactions"):
        assert len(transactions) == 2

    transaction_page.generate_report_csv(transactions)
