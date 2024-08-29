from selenium.webdriver.common.by import By

login_link_on_forgot_password = (By.XPATH, "//a[text() = 'Восстановить пароль']")
login_email_input = (By.XPATH, ".//input[@name = 'name']")
login_show_password = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
login_password_input = (By.XPATH, ".//input[@name = 'Пароль']")
login_password_reset = (By.XPATH, "//button[text() = 'Восстановить']")
login_button= (By.XPATH, './/button[text()="Войти"]')

