import allure
import page_urls
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage
from pages.reset_page import ResetPage


class TestResetPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_recovery_page(self, driver):
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)

        driver.get(page_urls.LOGIN_PAGE)
        login_page.click_restore_password()
        recovery_page.wait_for_recovery_page_loaded()
        result_url = recovery_page.get_current_url()

        assert result_url == page_urls.RECOVERY_PAGE

    @allure.title('Проверка переход на страницу сброса пароля по кнопке «Восстановить»')
    def test_open_reset_page(self, driver):
        recovery_page = RecoveryPage(driver)
        reset_page = ResetPage(driver)

        driver.get(page_urls.RECOVERY_PAGE)
        recovery_page.fill_email_field('Elina@email.ru')
        recovery_page.click_recovery_button()
        reset_page.wait_for_reset_page_loaded()
        result_url = recovery_page.get_current_url()

        assert result_url == page_urls.RESET_PAGE

    @allure.title('Проверка: по клику на кнопку "показать пароль" подсвечивается поле')
    def test_show_password(self, driver):
        recovery_page = RecoveryPage(driver)
        reset_page = ResetPage(driver)

        driver.get(page_urls.RECOVERY_PAGE)
        recovery_page.fill_email_field('Elina@email.ru')
        recovery_page.click_recovery_button()
        reset_page.wait_for_reset_page_loaded()
        reset_page.click_on_show_password()
        element_class = reset_page.get_password_field_class()

        assert 'input_status_active' in element_class