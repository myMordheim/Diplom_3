from selenium.webdriver.common.by import By

order = (By.XPATH, './/h2[@class="text text_type_main-medium mb-2"][1]')
modal = (By.XPATH, '//p[text()="Cостав"]')
title = (By.XPATH, '//h1[text()="Лента заказов"]')
counter_all_time = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
counter_today = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
counter_progress = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
order_window = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
order_history = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
check_order = (By.XPATH, f'.//p[@class="text text_type_digits-default"]')

