import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from functions import AppiumTest

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='9ff9d5c1',
    platformVersion='11',
    language='en',
    locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'


@pytest.fixture(scope="function")
def driver():
    app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app_driver  # Yield the driver instance instead of None
    if app_driver:
        app_driver.quit()


def press_on_site():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(312, 895)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


@allure.suite("Basic mobile test")
def test_find_battery(driver):
    test = AppiumTest()
    test.open_chrome(driver)



    # actions = ActionChains(driver)# Pass the driver fixture as an argument
    # chrome = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Chrome"]')
    # chrome.click()
    # time.sleep(2)
    # search_bar = driver.find_element(AppiumBy.ID, 'com.android.chrome:id/search_box_text')
    # search_bar.send_keys('https://www.kingbillycasino.com')
    # time.sleep(2)
    # option_site = driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.android.chrome:id/omnibox_suggestions_dropdown"]/android.view.ViewGroup[2]/android.widget.LinearLayout')
    # option_site.click()
    # time.sleep(2)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(312, 895)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(5)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(560, 2201)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(224, 1922)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(409, 1508)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(514, 864)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(61, 1627)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(909, 1629)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(279, 1627)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(704, 1632)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(812, 1621)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(594, 1624)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(69, 2044)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(113, 1903)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(224, 2044)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(867, 2187)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # time.sleep(2)
    #
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(588, 1047)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.pause(0.1)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
