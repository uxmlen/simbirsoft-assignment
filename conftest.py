from datetime import datetime

import allure
import pytest
from allure import attachment_type
from selenium import webdriver

from config import GRID_CONNECTION_IP


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Remote(
        command_executor=f"{GRID_CONNECTION_IP}/wd/hub",
        options=webdriver.FirefoxOptions(),
    )
    driver.implicitly_wait(10)

    yield driver

    screenshot = driver.get_screenshot_as_png()
    allure.attach(
        screenshot,
        name=f"Quitting {datetime.now()}",
        attachment_type=attachment_type.PNG,
    )

    driver.quit()
