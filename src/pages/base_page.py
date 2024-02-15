import logging
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""
This BasePage class serves as the foundation for all page objects within the framework,
centralizing common functionalities and properties.Integrates an action handler for performing actions like clicks and text inputs,
equipped to handle intermediate elements like pop-ups or modals dynamically encountered during tests.
The class provides a mechanism to update the web driver instance, ensuring actions are performed
using the current session's driver, facilitating seamless test execution across different pages.
"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        logging.info(f"Base Page driver session id {self.driver.session_id}")


    def _perform_with_retry(self, operation, locator, max_attempts=3, *args, **kwargs):
        """
        Retries an operation on an element, handling intermediate elements if necessary.
        """
        last_exception = None
        for attempt in range(max_attempts):
            try:
                # if attempt > 0:
                #     # Handle intermediate elements before retrying
                #     self._handle_intermediate_elements()
                return operation(locator, *args, **kwargs)
            except (TimeoutException, WebDriverException) as e:
                logging.error(f"Attempt {attempt + 1} failed for {locator}: {e}")
                last_exception = e
        raise last_exception  # Raise the last exception if all attempts fail

    def get_element(self, locator):
        """Waits for an element to be visible and returns it, with retries."""
        action = lambda loc: WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc))
        return self._perform_with_retry(action, locator)

    def send_keys(self, locator, send_text):
        """Sends text to the element"""
        action = lambda loc: WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc)).send_keys(
            send_text)
        self._perform_with_retry(action, locator)

    def click(self, locator):
        """Waits for an element to be clickable and then clicks it, with retries."""
        logging.info(f"Click function session id: {self.driver.session_id}")
        action = lambda loc: WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc)).click()
        self._perform_with_retry(action, locator)
