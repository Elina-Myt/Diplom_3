import allure
import page_urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверка перехода по кнопке "Личный кабинет" в профиль пользователя')
    def test_open_profile_page(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        driver.get(page_urls.LOGIN_PAGE)
        login_page.fill_user_data_form(registered_user['email'], registered_user['password'])
        main_page.click_profile_link()
        user_name = profile_page.get_text_from_name_field()

        assert user_name == registered_user['name']

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_open_order_history(self, driver, authorize_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        driver.get(page_urls.BASE_URL)
        main_page.click_profile_link()
        profile_page.click_order_history_link()
        result_url = profile_page.get_current_url()

        assert result_url == page_urls.ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, authorize_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)

        driver.get(page_urls.BASE_URL)
        main_page.click_profile_link()
        profile_page.click_exit_button()
        profile_page.wait_for_login_page_loaded()
        result_url = profile_page.get_current_url()

        assert result_url == page_urls.LOGIN_PAGE