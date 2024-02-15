from behave import *
from pages.account_page import AccountPage
from pages.camera_page import CameraPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage

use_step_matcher("re")


@given("user is at Profile Page")
def step_impl(context):
    home_page = HomePage(context)
    home_page.click_menu()

    account_page = AccountPage(context)
    account_page.click_profile_name()


@when("user changes first name with (?P<first_name>.+), last name with (?P<last_name>.+) and taps Done button")
def step_impl(context, first_name, last_name):
    profile_page = ProfilePage(context)
    profile_page.input_first_name(first_name)
    profile_page.input_last_name(last_name)
    profile_page.click_done()


@then("Account Page is shown")
def step_impl(context):
    account_page = AccountPage(context)
    assert account_page.get_account_title() == 'Account'


@step("old name was changed with (?P<first_name>.+) (?P<last_name>.+)")
def step_impl(context, first_name, last_name):
    account_page = AccountPage(context)
    full_name = f'{first_name} {last_name}'
    assert account_page.get_profile_name() == full_name
    account_page.click_done_button()


@when("user takes a picture with the device camera")
def step_impl(context):
    profile_page = ProfilePage(context)
    profile_page.click_camera()
    profile_page.select_camera()
    profile_page.click_allow_this_time()

    camera_page = CameraPage(context)
    camera_page.click_shutter_camera()
    camera_page.click_done_button()
    camera_page.click_done_menu()

    profile_page.click_done()


@step("small picture is shown next to the name")
def step_impl(context):
    account_page = AccountPage(context)
    assert account_page.get_avatar() is not None
    account_page.click_done_button()
