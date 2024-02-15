from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

'''
Page elements and methods related to Phone Number Page
'''


class ProfilePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver)

    _first_name_input = (AppiumBy.ID, "com.hdw.james.rider:id/firstNameInput")
    _last_name_input = (AppiumBy.ID, "com.hdw.james.rider:id/lastNameInput")
    _done_button = (AppiumBy.ID, "com.hdw.james.rider:id/DEFAULT_TEXT_ACTION_MENU_ID")
    _camera_button = (AppiumBy.ID, "com.hdw.james.rider:id/profileCameraButton")
    _camera_pick = (AppiumBy.ID, "com.hdw.james.rider:id/imagePickerCameraRow")
    _allow_this_time = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button")
    _allow_while_using = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    _allow_dont_allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")

    def input_first_name(self, first_name):
        self.send_keys(self._first_name_input, first_name)

    def input_last_name(self, last_name):
        self.send_keys(self._last_name_input, last_name)

    def click_allow_this_time(self):
        self.click(self._allow_this_time)

    def click_allow_while_using(self):
        self.click(self._allow_while_using)

    def click_deny_permission(self):
        self.click(self._allow_dont_allow)

    def click_done(self):
        self.click(self._done_button)

    def click_camera(self):
        self.click(self._camera_button)

    def select_camera(self):
        self.click(self._camera_pick)
