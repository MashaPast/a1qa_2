from t5_userinyerface.base_items.base_element import BaseElement
from t5_userinyerface.elements.user_form_item import UserFormItem


class UserForm(BaseElement):
    def __init__(self, locator_res: tuple, locator: tuple):
        super().__init__(locator)
        self.auth = UserFormItem(locator_res)