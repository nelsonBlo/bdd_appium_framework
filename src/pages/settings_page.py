from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class SettingsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver)

    _account = (AppiumBy.XPATH,
                "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.hdw.james.rider:id/settingsMenuRecycler']/android.view.ViewGroup[1]")
