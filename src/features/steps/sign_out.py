import time

from behave import *

from pages.phone_number_page import PhoneNumberPage
from pages.account_page import AccountPage
from pages.home_page import HomePage

use_step_matcher("re")


@given("user is at Account Page")
def step_impl(context):
    home_page = HomePage(context)
    home_page.click_menu()

    account_page = AccountPage(context)
    assert account_page.get_account_title() == 'Account'


@when("user taps in sign out")
def step_impl(context):
    account_page = AccountPage(context)
    account_page.click_sign_out()


@then("app close session and shows phone number page")
def step_impl(context):
    time.sleep(3)
    phone_number_page = PhoneNumberPage(context)
    expected_text = 'Enter your phone number'
    assert phone_number_page.get_phone_number_text() == expected_text
