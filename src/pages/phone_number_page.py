from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class PhoneNumberPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver)

    _phone_number_title = (AppiumBy.ID, "com.hdw.james.rider:id/title")
    _phone_number_input = (AppiumBy.ID, "com.hdw.james.rider:id/input")
    _phone_number_continue = (AppiumBy.ID, "com.hdw.james.rider:id/continueButton")

    def input_number(self, number):
        self.send_keys(self._phone_number_input, number)

    def click_continue(self):
        self.click(self._phone_number_continue)

    def get_phone_number_text(self):
        return self.get_element(self._phone_number_title).text
