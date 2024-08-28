import allure
from conftest import *
from pages.forgot_password_page import *
from URLs import *


class TestLoginPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_forgot_password_redirect(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.change_url(URLS.login_page_url)
        forgot_page.click_forgot_password_button()
        assert forgot_page.get_current_url() == URLS.forgot_password

    @allure.title('Проверка восстановления пароля с заполненной почтой')
    def test_forgot_passwrod_with_correct_email_input(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.change_url(URLS.login_page_url)
        forgot_page.click_forgot_password_button()
        forgot_page.fill_input_email('Galadriel')
        forgot_page.click_reset_pass()
        assert forgot_page.get_current_url() == URLS.forgot_password

    @allure.title('Проверка функционала отображения пароля')
    def test_show_password_button(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.change_url(URLS.login_page_url)
        forgot_page.fill_input_password('Galadriel')
        forgot_page.click_password_visible()
        assert forgot_page.active_password_input
