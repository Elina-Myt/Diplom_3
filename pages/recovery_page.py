import allure
import page_urls
from locators.recovery_page_locators import RecoveryPageLocators
from pages.base_page import BasePage


class RecoveryPage(BasePage):

    @allure.step('Ожидание загрузки страницы Восстановления пароля')
    def wait_for_recovery_page_loaded(self):
        self.wait_for_url(page_urls.RECOVERY_PAGE)

    @allure.step('Заполнение поля emai')
    def fill_email_field(self, email):
        self.find_element_with_wait(RecoveryPageLocators.EMAIL_FIELD)
        self.set_text_to_form(RecoveryPageLocators.EMAIL_FIELD, email)

    @allure.step('Кликнуть кнопку Восстановить')
    def click_recovery_button(self):
        self.find_element_with_wait(RecoveryPageLocators.RESTORE_BUTTON)
        self.click_on_element(RecoveryPageLocators.RESTORE_BUTTON)
