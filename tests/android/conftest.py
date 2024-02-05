import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
from settings import user_credentials
import os


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities(
        {
            "platformVersion": "12.0",
            "deviceName": "Samsung Galaxy S21",
            "app": "bs://sample.app",
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": user_credentials.user_name,
                "accessKey": user_credentials.access_key,
            },
        }
    )

    browser.config.driver_remote_url = user_credentials.remote_url
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
