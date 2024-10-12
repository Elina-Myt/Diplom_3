from selenium.webdriver.common.by import By


class FeedPageLocators:
    # первый заказ в ленте
    FIRST_ORDER = By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]'
    # Модельное окно деталей заказа
    ORDER_MODAL_HEADER = By.XPATH, ('.//div[contains(@class, "Modal_orderBox")]'
                                    '/parent::div[contains(@class, "Modal_modal__container")]'
                                    '/parent::section[contains(@class, "Modal_modal_opened")]')
    # номер заказа первого элемента в Ленте заказов
    ORDERS = By.XPATH, ('.//div[contains(@class, "OrderFeed_contentBox")]'
                        '/ul[contains(@class, "OrderFeed_list")]'
                        '/li[contains(@class, "OrderHistory_listItem")][1]'
                        '/a[contains(@class, "OrderHistory_link")]'
                        '/div[contains(@class, "OrderHistory_textBox")]'
                        '/p[@class = "text text_type_digits-default"]')
    # номер заказа в списке заказов "В работе"
    ORDER_IN_WORK = By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li'
    # надпись "Все текущие заказы готовы!" в списке заказов "В работе"
    EMPTY_ORDERS_IN_WORK = By.XPATH, './/li[text()="Все текущие заказы готовы!"]'
    # счетчик заказов за все время
    ORDER_COUNTER_ALL_TIME = By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p"
    # счетчик заказов за сегодня
    ORDER_COUNTER_BY_DAY = By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p"
