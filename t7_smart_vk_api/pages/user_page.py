from string import Template
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from t7_smart_vk_api.base_items.default_page import BasePage
from t7_smart_vk_api.elements.button import Button
from t7_smart_vk_api.elements.post import Post


class UserPage(BasePage):
    MY_PAGE = Button((By.ID, 'l_pr'))
    POST = (Template('//*[contains(text(), "$message")]'))
    POST_PICTURE = (Template('//*[@data-photo-id="$pic_id"]'))
    COMMENTS_TO_POST = (Template('//*[@id="replies$post"]/a'))
    COMMENT_BY_OWNER_ID = (Template('//*[@id="post$post"]//a[@data-from-id="$owner_id"]'))
    POSTS_LIKE = (Template('//*[@id="post$post"]//div[@class="like_button_icon"]'))

    def click_my_page(self):
        self.MY_PAGE.click()

    def find_post(self, message):
        post_by_message = (By.XPATH, UserPage.POST.substitute(message=message))
        return self.find_element(post_by_message)

    @staticmethod
    def get_onclick_attribute( pic_id):
        picture_post = Post((By.XPATH, UserPage.POST_PICTURE.substitute(pic_id=pic_id)))
        return picture_post.get_attribute('onclick')

    @staticmethod
    def show_comments_to_post(post):
        show_comments = Button((By.XPATH, UserPage.COMMENTS_TO_POST.substitute(post=post)))
        show_comments.click()

    def get_comment_by_ids(self, post_id, user_id):
        owner_id_comment = (By.XPATH, UserPage.COMMENT_BY_OWNER_ID.substitute(
            post=post_id, owner_id=user_id))
        return self.find_element(owner_id_comment)

    @staticmethod
    def like_post(post_id):
        like_by_id = Button((By.XPATH, UserPage.POSTS_LIKE.substitute(post=post_id)))
        like_by_id.click()

    def check_post_deleted(self, message):
        post_by_message = (By.XPATH, UserPage.POST.substitute(message=message))
        try:
            self.find_element(post_by_message)
            return False
        except TimeoutException:
            return True