from pages.base_page import *
from URLs import *
from locators import personal_account_locators


class PersonalAccountPage(BasePage):

    @allure.step('Открыть страницу личного профиля переходом по URL')
    def pa_link(self):
        self.change_url(URLS.base_url)

    @allure.step('Открывыть страницу личного профиля')
    def click_pa_page(self):
        self.click_element(personal_account_locators.personal_account)

    @allure.step('Открыть страницу истории заказов')
    def click_history(self):
        self.click_element(personal_account_locators.history_button)

    @allure.step('Проверить, что окно с историей заказов отображается')
    def check_history_window(self):
        self.find_element(personal_account_locators.history_item_window)

    @allure.step('Проверить страницу профиля')
    def check_pa_redirect_page(self):
        return self.find_element(personal_account_locators.profile_button)

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click_element(personal_account_locators.logout)