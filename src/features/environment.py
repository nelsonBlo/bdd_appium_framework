from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options


def before_feature(context, feature):
    capabilities = {
        "platformName": "Android",
        "appium:deviceName": "Pixel_3a",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": True,
        "appium:appPackage": "com.hdw.james.rider",
        "appium:appActivity": "com.hdw.james.rider.viewlayer.launcher.LauncherActivity"
    }
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723', options=UiAutomator2Options().load_capabilities(capabilities))


def after_feature(context, feature):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_final.png")
    context.driver.quit()
