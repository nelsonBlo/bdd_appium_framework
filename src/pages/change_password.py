from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ChangePassword(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver)

    _current_password = (AppiumBy.ID, "com.hdw.james.rider:id/currentPasswordInput")
    _new_password = (AppiumBy.ID, "com.hdw.james.rider:id/newPasswordInput")
    _done_button = (AppiumBy.ID, "com.hdw.james.rider:id/DEFAULT_TEXT_ACTION_MENU_ID")

    def input_current_password(self, current_password):
        self.send_keys(self._current_password, current_password)

    def input_new_password(self, new_password):
        self.send_keys(self._new_password, new_password)

    def click_done_button(self):
        self.click(self._done_button)
