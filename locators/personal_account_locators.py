from selenium.webdriver.common.by import By

profile_button = (By.XPATH, ".//a[text() = 'Профиль']")
history_button = (By.XPATH, ".//a[text() = 'История заказов']")
history_item_window = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
logout = (By.XPATH, ".//button[text() = 'Выход']")
personal_account = (By.XPATH, './/p[text()="Личный Кабинет"]')