from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
from config import LOGIN, PASS
import time


class general:
    def __init__(self) -> None:
        # Инициализация драйвера
        chrome_options = Options()

        # Опция --disable-dev-shm-usage отключает использование разделяемой памяти /dev/shm в Chrome, 
        # что может быть полезно в случае проблем с доступом к памяти в виртуальной машине или 
        # контейнере Docker при использовании Selenium.
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Опция UserAgent().random в ChromeOptions устанавливает случайный пользовательский агент, 
        # что может быть полезно при скрытии фактического типа браузера и его версии от веб-сайта 
        # при скрапинге данных или тестировании веб-приложений.
        chrome_options.add_argument(UserAgent().random)

        # Опция --no-sandbox отключает защищенный режим (sandbox) Chrome
        chrome_options.add_argument('--no-sandbox')

        # Опция --headless в ChromeOptions включает "безголовый" (headless) режим запуска браузера 
        # Chrome, который позволяет работать с браузером без его графического интерфейса.
        chrome_options.add_argument('--headless')
        
        # Эта строка кода создает экземпляр драйвера Chrome WebDriver с заданными настройками, 
        # которые указаны в объекте chrome_options. Это позволяет выполнить скрипты автоматизации 
        # в Chrome браузере с нужными настройками.
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

        # Ссылка на сайт
        self.url = 'https://lalafo.kg/'

        # Логин и пароль
        self.LOGIN = LOGIN
        self.PASS = PASS

    def autorise(self, email_or_phone_number, password):
        """Функция авторизации, при вызове нужно передать ссылку, почту или номер телефона и пароль"""
        wait = WebDriverWait(self.driver, 20)
        self.driver.get(url=self.url)
        time.sleep(5)
        enter_button = self.driver.find_element(By.CLASS_NAME, 'main-header__user-menu').click()
        input_email_or_phone_number = self.driver.find_element(By.CLASS_NAME, 'LFInput__input ')
        time.sleep(8)
        input_email_or_phone_number.clear()
        input_email_or_phone_number.send_keys(email_or_phone_number)
        time.sleep(2)
        input_password = self.driver.find_element(By.CLASS_NAME, 'LFInputPassword__input  ').send_keys(password)
        time.sleep(2)
        enter_button2 = self.driver.find_element(By.CLASS_NAME, 'login-form__controls').click()
        time.sleep(10)

    def send_message(self, url, message):
        '''Функция по отправке сообщений, при вызове передаем ссылку на обЪявление, и текст сообщения'''
        self.driver.get(url=url)
        time.sleep(5)  
        message_text = self.driver.find_element(By.CLASS_NAME, 'msg-input').send_keys(message)
        time.sleep(5)
        send_message_button = self.driver.find_element(By.CLASS_NAME, 'LFButton.large.primary-green').click()
        time.sleep(5)

    def main(self):
        try:
            self.autorise(LOGIN, PASS)
            self.send_message('https://lalafo.kg/bishkek/ads/srocno-prodaetsa-3h-komn-kv-cuj-gogola-id-106344153', 
            'Здравствуйте')
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()

if __name__ == '__main__':
    general().main()