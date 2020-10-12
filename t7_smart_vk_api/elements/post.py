from t7_smart_vk_api.base_items.base_element import BaseElement


class Post(BaseElement):
    def __init__(self, locator: tuple):
        super().__init__(locator)

    def get_attribute(self, attr):
        return self.find_element().get_attribute(attr)