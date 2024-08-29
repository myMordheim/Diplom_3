from conftest import *
from pages.order_page import OrderPage
from pages.main_function_page import *
from pages.forgot_password_page import *
from pages.personal_accout_page import *
from helpers import *


class TestFeedPage:

    @allure.title('Проверяем модальное окно в истории заказов')
    def test_click_feed_open_modal(self, driver):
        main_page = MainFunctionPage(driver)
        forgot_page = ForgotPasswordPage(driver)
        order_page = OrderPage(driver)
        forgot_page.change_url(URLS.login_page_url)
        forgot_page.login()
        main_page.click_list()
        order_page.click_order()
        assert order_page.check_modal()

    @allure.title('Проверяем, что заказы пользователя отображатся в истории заказов')
    def test_order_user_shown_in_feed(self, driver):
        main_page = MainFunctionPage(driver)
        forgot_page = ForgotPasswordPage(driver)
        order_page = OrderPage(driver)
        pa_page = PersonalAccountPage(driver)
        forgot_page.change_url(URLS.login_page_url)
        forgot_page.login()
        main_page.bun_drag_drop()
        main_page.create_order()
        pa_page.pa_link()
        pa_page.click_pa_page()
        pa_page.click_history()
        order_id = order_page.get_order_id()
        main_page.click_list()
        assert order_page.check_order(order_id)

    @allure.title('Проверяем счетчик всех заказов')
    def test_feed_all_orders_counter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        count = order_page.get_order_count_all()
        create_order()
        assert int(order_page.get_order_count_all()) > int(count)

    @allure.title('Проверяем счетчик заказов за сегодня')
    def test_feed_today_orders_counter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        count = order_page.get_order_count_today()
        create_order()
        assert int(order_page.get_order_count_today()) > int(count)

    @allure.title('Проверяем что заказы в работе корректно отображатся')
    def test_feed_in_work_id(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_id = create_order()
        assert order_id == int(order_page.get_order_in_work_id())