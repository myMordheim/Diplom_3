from conftest import *
from pages.main_function_page import *
from pages.forgot_password_page import *
from data import *


class TestMainPage:

    @allure.title('Перейти в конструктор')
    def test_click_constructor(self, driver):
        main_page = MainFunctionPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        main_page.click_constructor()
        assert main_page.get_current_url() == URLS.base_url

    @allure.title('Перейти в ленту заказов')
    def test_click_list(self, driver):
        main_page = MainFunctionPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        main_page.click_list()
        assert main_page.get_current_url() == URLS.order_url

    @allure.title('Проверка модального окна ингридиентов')
    def test_click_bun(self, driver):
        main_page = MainFunctionPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        main_page.click_constructor()
        main_page.click_bun()
        assert main_page.get_current_url() == URLS.bun_url

    @allure.title('Проверка закрытия модального окна')
    def test_close_modal_bun(self, driver):
        main_page = MainFunctionPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        main_page.click_constructor()
        main_page.click_bun()
        main_page.close_modal()
        assert not main_page.modal_window

    @allure.title('Проверить, что после добавление ингридиента счетчик увеличился')
    def test_count_in_basket(self, driver):
        main_page = MainFunctionPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        main_page.click_constructor()
        main_page.bun_drag_drop()
        assert main_page.check_count() == '2'

    @allure.title('Проверка создания заказа')
    def test_create_order(self, driver):
        main_page = MainFunctionPage(driver)
        login_page = ForgotPasswordPage(driver)
        login_page.change_url(URLS.login_page_url)
        login_page.login()
        main_page.click_constructor()
        main_page.bun_drag_drop()
        main_page.create_order()
        assert main_page.text_order()