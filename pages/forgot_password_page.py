import allure
from locators import forgot_password_locators
from pages.base_page import BasePage
from data import *


class ForgotPasswordPage(BasePage):

    @allure.step("Нажать на баттон восстановить пароль")
    def click_forgot_password_button(self):
        self.click_element(forgot_password_locators.login_link_on_forgot_password)

    @allure.step("Нажать на кнопку восстановить")
    def click_reset_pass(self):
        self.click_element(forgot_password_locators.login_password_reset)

    @allure.step("Заполнить инпут email")
    def fill_input_email(self, email):
        self.send_text(forgot_password_locators.login_email_input, email)

    @allure.step("Заполнить инпут пароль")
    def fill_input_password(self, password):
        self.send_text(forgot_password_locators.login_password_input, password)

    @allure.step('Проверяем активно ли поле ввода пароля')
    def active_password_input(self):
        return 'input_status_active' in self.get_attribute(forgot_password_locators.login_password_input, 'class')

    @allure.step('Нажать на баттон отображения пароля')
    def click_password_visible(self):
        self.click_element(forgot_password_locators.login_show_password)

    @allure.step("Нажать на баттон входа")
    def click_button_login(self):
        self.click_element(forgot_password_locators.login_button)

    @allure.step('Логин зарегестрированного пользователя')
    def login(self):
        self.fill_input_email(user_data[0])
        self.fill_input_password(user_data[1])
        self.click_button_login()

    def wait_for_visability(self):
        self.wait_for_element_visability(forgot_password_locators.login_link_on_forgot_password)