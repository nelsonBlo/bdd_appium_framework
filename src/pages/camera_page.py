from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CameraPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver)

    _shutter_button = (AppiumBy.ID, "com.android.camera2:id/shutter_button")
    _done_button = (AppiumBy.ID, "com.android.camera2:id/done_button")
    _done_menu = (AppiumBy.ID, "com.hdw.james.rider:id/menu_crop")

    def click_shutter_camera(self):
        self.click(self._shutter_button)

    def click_done_button(self):
        self.click(self._done_button)

    def click_done_menu(self):
        self.click(self._done_menu)
