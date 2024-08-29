from selenium.webdriver.common.by import By

constructor = (By.XPATH, './/p[text()="Конструктор"]')
order_list = (By.XPATH, './/p[text()="Лента Заказов"]')
bun = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
close_modal = (By.XPATH, '//button[contains(@class,"close")]')
busket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
counter = (By.XPATH, './/p[@class="counter_counter__num__3nue1"]')
create_order = (By.XPATH, './/button[text()="Оформить заказ"]')
text_order = (By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]')