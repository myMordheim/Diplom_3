from pages.base_page import BasePage
from URLs import URLS
from locators import main_function_locators
#from seletools.actions import drag_and_drop
import allure


class MainFunctionPage(BasePage):
    @allure.step("Переход в конструктор")
    def click_constructor(self):
        self.click_element(main_function_locators.constructor)

    @allure.step("Переход в ленту заказов")
    def click_list(self):
        self.click_element(main_function_locators.order_list)

    @allure.step('Нажать на булку')
    def click_bun(self):
        self.click_element(main_function_locators.bun)

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click_element(main_function_locators.close_modal)

    @allure.step('Проверить открыто ли модальное окно')
    def modal_window(self):
        return 'Modal_modal_opened__3ISw4' in self.get_attribute(main_function_locators.close_modal, 'class')


    @allure.step('Добавляем булочку в корзину')
    def bun_drag_drop(self):
        self.drag_drop(main_function_locators.bun, main_function_locators.busket)

    @allure.step('Проверяем количество булочек в корзине')
    def check_count(self):
        return self.find_text_element(main_function_locators.counter)

    @allure.step('Создаем заказ')
    def create_order(self):
        self.click_element(main_function_locators.create_order)

    @allure.step('Проверяем, что заказ создан')
    def text_order(self):
        return 'Ваш заказ начали готовить' in self.find_text_element(main_function_locators.text_order)