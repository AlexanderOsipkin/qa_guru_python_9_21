import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.title("iPhone 15 Pro")
def test_search_ios():
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type(
            "qa guru" + "\n"
        )
        text_output = browser.element(
            (AppiumBy.ACCESSIBILITY_ID, "Text Output")
        ).should(be.clickable)

    with allure.step('Verify content'):
        text_output.should(have.text("qa guru"))
