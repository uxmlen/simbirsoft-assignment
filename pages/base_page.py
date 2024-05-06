import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self._driver = driver
        self._url = url

    @allure.step("Open the page")
    def open(self):
        self._driver.get(self._url)

    @allure.step("Find element visible")
    def element_is_visible(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Find elements visible")
    def elements_are_visible(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Select option")
    def choice_option(self, locator: tuple[str, str], text: str):
        select_element = self._driver.find_element(*locator)
        Select(select_element).select_by_visible_text(text)
