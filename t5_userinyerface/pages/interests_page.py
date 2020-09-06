from selenium.webdriver.common.by import By
from t5_userinyerface.default_page.default_page import BasePage
from t5_userinyerface.elements.elements import Button, CheckBox



class InterestsPage(BasePage):

    UNSELECT = (By.XPATH, './/*[contains(@for, "interest_unselectall")]')
    CLOSETS = (By.XPATH, './/*[contains(@for, "interest_closets")]')
    BALLS = (By.XPATH, './/*[contains(@for, "interest_balls")]')
    SQUARES = (By.XPATH, './/*[contains(@for, "interest_squares")]')
    DOWNLOAD = (By.XPATH, './/*[text()="upload"]')
    NEXT_BUTTON = (By.XPATH, './/*[text()="Next"]')

    def __init__(self, driver):
        super().__init__(driver)

    def unselect_in_checkbox(self):
        return CheckBox(InterestsPage.UNSELECT, self.driver).select_in_checkbox()

    def select_in_checkbox(self):
        CheckBox(InterestsPage.CLOSETS, self.driver).select_in_checkbox()
        CheckBox(InterestsPage.BALLS, self.driver).select_in_checkbox()
        CheckBox(InterestsPage.SQUARES, self.driver).select_in_checkbox()

    def upload_image(self, path):
        Button(InterestsPage.DOWNLOAD, self.driver).upload_image(path)

    def click_next(self):
        Button(InterestsPage.NEXT_BUTTON, self.driver).click_on_button()