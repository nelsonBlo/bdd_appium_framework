from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver)

    _snackbar = (AppiumBy.ID, "com.hdw.james.rider:id/snackbar_text")
    _profile_name = (AppiumBy.ID, "com.hdw.james.rider:id/profileName")
    _account_title = (AppiumBy.XPATH, "//android.widget.TextView[@text='Account']")
    _settings = (
    AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.hdw.james.rider:id/title' and @text='SETTINGS']")
    _change_password = (AppiumBy.XPATH,
                        "//android.widget.TextView[@resource-id='com.hdw.james.rider:id/title' and @text='CHANGE PASSWORD']")
    _sign_out = (AppiumBy.XPATH,
                 "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.hdw.james.rider:id/actionList']/android.view.ViewGroup[5]")
    _avatar = (AppiumBy.ID, "com.hdw.james.rider:id/avatar")
    _done_button = (AppiumBy.ID, "com.hdw.james.rider:id/DEFAULT_TEXT_ACTION_MENU_ID")

    def click_profile_name(self):
        self.click(self._profile_name)

    def get_profile_name(self):
        return self.get_element(self._profile_name).text

    def get_account_title(self):
        return self.get_element(self._account_title).text

    def get_snackbar_text(self):
        return self.get_element(self._snackbar).text

    def click_sign_out(self):
        self.click(self._sign_out)

    def get_avatar(self):
        return self.get_element(self._avatar)

    def click_done_button(self):
        self.click(self._done_button)
