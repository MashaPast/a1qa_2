from selenium.webdriver.common.by import By
from t5_userinyerface.base_items.default_page import BasePage
from t5_userinyerface.elements.checkbox import CheckBox
from t5_userinyerface.elements.button import Button
from t5_userinyerface.helpers.helpers import encode_image_with_base64

class InterestsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.UNSELECT = CheckBox((By.XPATH, '//*[contains(@for, "interest_unselectall")]'), driver)
        self.CLOSETS = CheckBox((By.XPATH, '//*[contains(@for, "interest_closets")]'), driver)
        self.BALLS = CheckBox((By.XPATH, '//*[contains(@for, "interest_balls")]'), driver)
        self.SQUARES = CheckBox((By.XPATH, '//*[contains(@for, "interest_squares")]'), driver)
        self.UPLOAD = Button((By.XPATH, '//div[@class = "avatar-and-interests__avatar-image"]'), driver)
        self.NEXT_BUTTON = Button((By.XPATH, '//a[contains(text(), "Next")]'), driver)

    def unselect_in_checkbox(self):
        return self.UNSELECT.click()

    def select_in_checkbox(self):
        self.CLOSETS.click()
        self.BALLS.click()
        self.SQUARES.click()

    def upload_image(self):
        base64_im = encode_image_with_base64()
        print(base64_im)
        element = self.UPLOAD.find_element()
        self.driver.execute_script("arguments[0].setAttribute('style','{}')".format(base64_im), element)

    def click_next(self):
        self.NEXT_BUTTON.click()
