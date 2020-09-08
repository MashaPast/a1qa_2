from selenium.webdriver.common.by import By
from t5_userinyerface.default_page.default_page import BasePage
from t5_userinyerface.elements.elements import Button, UserForm
from t5_userinyerface.helpers.helpers import generate_random_pass, generate_random_str


class AuthPage(BasePage):

    COOKIE_FORM = (By.XPATH, '//*[@id="app"]/div/div[1]')
    ACCEPT_COOKIE = (By.XPATH, './/*[text() = "Not really, no"]')
    SEND_TO_BUTTON = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/button')
    HELP_FORM_IS_HIDDEN = (By.XPATH, './/*[contains(@class, "help-form is-hidden")]')
    TIMER = (By.XPATH, './/*[contains(@class, "timer timer--white timer--center")]')
    #Button(AuthPage.ACCEPT_COOKIE, self.driver)

    def __init__(self, driver):
        super().__init__(driver)

    def click_send_to_button(self):
        return Button(AuthPage.SEND_TO_BUTTON, self.driver).click_on_button()

    def check_help_window_is_closed(self):
        return Button(AuthPage.HELP_FORM_IS_HIDDEN, self.driver).check_form_exists()

    def get_time_from_timer(self):
        return Button(AuthPage.TIMER, self.driver).get_text()

    def click_to_accept_cookie(self):
        return Button(AuthPage.ACCEPT_COOKIE, self.driver).click_on_button()

    def check_cookie_form_is_open(self):
        return Button(AuthPage.ACCEPT_COOKIE, self.driver).check_form_exists()

    def get_all_cookies(self) -> list:
        return self.driver.get_cookies()




class UserFormAuthPage(BasePage):
    CARD_NUM = (By.XPATH, './/*[contains(@class, "page-indicator")]')
    PASS_FIELD = (By.XPATH, './/*[contains(@placeholder, "Choose Password")]')
    EMAIL_FIELD = (By.XPATH, './/*[contains(@placeholder, "Your email")]')
    DOMAIN_FIELD = (By.XPATH, './/*[contains(@placeholder, "Domain")]')
    ACCEPT_TERMS_CHECKBOX = (By.XPATH, './/*[contains(@class, "icon icon-check checkbox__check")]')
    DOMAIM_DROP_DOWN = (By.XPATH, './/*[contains(@class, "icon icon-chevron-down")]')
    NEXT_BUTTON = (By.XPATH, './/*[contains(@class, "button--secondary")]')
    DROP_DOWN = (By.XPATH, './/*[contains(@class, "dropdown__field")]')


    def check_card_is_opened(self):
        num_field = UserForm(UserFormAuthPage.CARD_NUM, self.driver)
        return num_field.auth.get_num_of_card()

    def clear_pass(self):
        pass_field = UserForm(UserFormAuthPage.PASS_FIELD, self.driver)
        pass_field.auth.clear_field()

    def clear_email(self):
        pass_field = UserForm(UserFormAuthPage.EMAIL_FIELD, self.driver)
        pass_field.auth.clear_field()

    def clear_domain(self):
        pass_field = UserForm(UserFormAuthPage.DOMAIN_FIELD, self.driver)
        pass_field.auth.clear_field()

    def fill_pass(self):
        password = generate_random_pass()
        pass_field = UserForm(UserFormAuthPage.PASS_FIELD, self.driver)
        pass_field.auth.send_text(password)

    def fill_email(self):
        email = generate_random_str()
        pass_field = UserForm(UserFormAuthPage.EMAIL_FIELD, self.driver)
        pass_field.auth.send_text(email)

    def fill_domain(self, domain):
        pass_field = UserForm(UserFormAuthPage.DOMAIN_FIELD, self.driver)
        pass_field.auth.send_text(domain)

    def click_to_accept_terms(self):
        terms = UserForm(UserFormAuthPage.ACCEPT_TERMS_CHECKBOX, self.driver)
        terms.auth.click()

    def click_next(self):
        next_button = UserForm(UserFormAuthPage.NEXT_BUTTON, self.driver)
        next_button.auth.click()

    def select_domain_in_drop_down(self, domain):
        domain_form = UserForm(UserFormAuthPage.DROP_DOWN, self.driver)
        domain_form.auth.select_domain(domain)
