import pytest
import os
from settings import user_credentials
from appium.options.ios import XCUITestOptions
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
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

    browser.config.driver_remote_url = user_credentials.remote_url
    browser.config.driver_options = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
