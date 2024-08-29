from pages.base_page import BasePage
from URLs import URLS
from locators import order_locators
import allure
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    @allure.step('Нажать на заказ')
    def click_order(self):
        self.click_element(order_locators.order)

    @allure.step('Проверить, что модальное окно открыто')
    def check_modal(self):
        return self.find_element(order_locators.modal)

    @allure.step('Получить номер последнего заказа')
    def get_order_id(self):
        return self.find_text_element(order_locators.order_history)[-1]

    @allure.step('Проверить, что заказ в списке')
    def check_order(self, order_id):
        self.find_element(order_locators.order)
        element = None
        elements = self.find_list_elements(order_locators.check_order)
        for e in elements:
            if order_id == e.text:
                element = e
                break
        return element

    @allure.step(f'Открываем страницу заказов')
    def open_order_page(self):
        self.driver.get(URLS.order_url)

    @allure.step('Получаем общее количество заказов')
    def get_order_count_all(self):
        return self.find_text_element(order_locators.counter_all_time)

    @allure.step('Получаем количество заказов за сегодня')
    def get_order_count_today(self):
        return self.find_text_element(order_locators.counter_today)

    @allure.step('Получаем номер заказа в работе')
    def get_order_in_work_id(self):
        return self.find_text_element(order_locators.counter_progress)
