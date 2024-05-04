import allure
from allure import attachment_type

from locators.auth_page_locators import AuthPageLocators

from .base_page import BasePage


class AuthPage(BasePage):
    """Authorization page"""

    locators = AuthPageLocators()

    @allure.step("Login as customer and submit")
    def login_as_customer(self, name: str):
        self.element_is_visible(self.locators.BUTTON_CUSTOMER_LOGIN).click()
        self.choice_option(self.locators.SELECTOR_YOUR_NAME, name)
        self.element_is_visible(self.locators.SUBMIT_BUTTON_LOGIN).click()

        screenshot = self._driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=f"Login as Customer",
            attachment_type=attachment_type.PNG,
        )
