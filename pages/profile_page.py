import allure
import page_urls
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Получить текст из поля "Имя"')
    def get_text_from_name_field(self):
        name = self.find_element_with_wait(ProfilePageLocators.NAME_FIELD).get_property('value')
        return name

    @allure.step('Кликнуть ссылку "История заказов"')
    def click_order_history_link(self):
        self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY).click()

    @allure.step('Кликнуть кнопку "Выход"')
    def click_exit_button(self):
        self.find_element_with_wait(ProfilePageLocators.EXIT_BUTTON)
        self.click_on_element(ProfilePageLocators.EXIT_BUTTON)

    @allure.step('Ожидание загрузки страницы авторизации')
    def wait_for_login_page_loaded(self):
        self.wait_for_url(page_urls.LOGIN_PAGE)

    def get_user_order(self):
        element = self.find_element_with_wait(ProfilePageLocators.ORDER_NUMBER)
        return element.text