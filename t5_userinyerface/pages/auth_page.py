from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from t5_userinyerface.base_items.default_page import BasePage
from t5_userinyerface.elements.button import Button
from t5_userinyerface.elements.user_form_item import UserFormItem
from t5_userinyerface.elements.user_form import UserForm
from t5_userinyerface.helpers.helpers import generate_random_pass, generate_random_str


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.ACCEPT_COOKIE = Button((By.XPATH, './/*[text() = "Not really, no"]'), driver)
        self.SEND_TO_BUTTON = Button((By.XPATH, '//button[contains(@class, "send-to-bottom-button")]'), driver)
        self.HELP_FORM_IS_HIDDEN = Button((By.XPATH, '//div[@class = "help-form is-hidden"]'), driver)
        self.TIMER = Button((By.XPATH, '//div[@class = "timer timer--white timer--center"]'), driver)

    def click_send_to_button(self):
        return self.SEND_TO_BUTTON.click()

    def check_help_window_is_closed(self):
        return self.HELP_FORM_IS_HIDDEN.check_form_exists()

    def get_time_from_timer(self):
        return self.TIMER.get_text()

    def click_to_accept_cookie(self):
        return self.ACCEPT_COOKIE.click()

    def check_cookie_form_is_open(self):
        return self.ACCEPT_COOKIE.check_form_exists()

    def get_all_cookies(self) -> list:
        return self.driver.get_cookies()


class UserFormAuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.CARD_NUM = UserFormItem((By.XPATH, '//div[@class = "page-indicator"]'), driver)
        self.PASS_FIELD = UserFormItem((By.XPATH, '//input[@placeholder = "Choose Password"]'), driver)
        self.EMAIL_FIELD = UserFormItem((By.XPATH, '//input[@placeholder = "Your email"]'), driver)
        self.DOMAIN_FIELD = UserFormItem((By.XPATH, '//input[@placeholder = "Domain"]'), driver)
        self.ACCEPT_TERMS_CHECKBOX = UserFormItem((By.XPATH, '//span[contains(@class, "icon icon-check checkbox__check")]'), driver)
        self.DOMAIN_DROP_DOWN = Button((By.XPATH, '//div[contains(@class, "dropdown__list")]'), driver)
        self.NEXT_BUTTON = UserFormItem((By.XPATH, '//a[contains(text(), "Next")]'), driver)

    def check_card_is_opened(self):
        return self.CARD_NUM.get_text()

    def clear_pass(self):
        self.PASS_FIELD.clear_field()

    def clear_email(self):
        self.EMAIL_FIELD.clear_field()

    def clear_domain(self):
        self.DOMAIN_FIELD.clear_field()

    def fill_pass(self):
        password = generate_random_pass()
        self.PASS_FIELD.send_text(password)

    def fill_email(self):
        email = generate_random_str()
        self.EMAIL_FIELD.send_text(email)

    def fill_domain(self, domain):
        self.DOMAIN_FIELD.send_text(domain)

    def click_to_accept_terms(self):
        self.ACCEPT_TERMS_CHECKBOX.click()

    def click_next(self):
        self.NEXT_BUTTON.click()

    def select_domain_in_drop_down(self, domain):
        select = Select(self.DOMAIN_DROP_DOWN.find_element())

        # select by visible text
        select.select_by_visible_text(domain)