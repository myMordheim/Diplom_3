from conftest import *
from pages.personal_accout_page import *
from pages.forgot_password_page import *
from URLs import URLS


class TestAccountPage:

    @allure.title('Проверить переход в личный кабинет')
    def test_login_click_account(self, driver):
        pa_page = PersonalAccountPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        pa_page.click_pa_page()
        pa_page.check_pa_redirect_page()
        assert pa_page.get_current_url() == URLS.personal_account_url

    @allure.title('Проверить переход в историю заказов')
    def test_login_click_feed(self, driver):
        pa_page = PersonalAccountPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        pa_page.click_pa_page()
        pa_page.check_pa_redirect_page()
        pa_page.click_history()
        assert pa_page.get_current_url() == URLS.order_history

    @allure.title('Проверить логаут в личном кабинете')
    def test_login_click_quit(self, driver):
        pa_page = PersonalAccountPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        pa_page.click_pa_page()
        pa_page.check_pa_redirect_page()
        pa_page.logout()
        login_page.wait_for_visability()
        assert pa_page.get_current_url() == URLS.login_page_url