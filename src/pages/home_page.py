from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver,
        )

    _menu = (AppiumBy.ID, "com.hdw.james.rider:id/MAIN_MENU_ID")

    def click_menu(self):
        self.click(self._menu)
