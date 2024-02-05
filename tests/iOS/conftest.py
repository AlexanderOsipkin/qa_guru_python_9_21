import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selene import browser
from settings import user_credentials
import os


@pytest.fixture(scope='function', autouse=True)
def mobile_management_ios():
    options = XCUITestOptions().load_capabilities(
        {
            "deviceName": "iPhone 15 Pro",
            "platformName": "ios",
            "platformVersion": "17",
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
    browser.config.driver = webdriver.Remote(
        user_credentials.remote_url, options=options
    )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
