import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем параметр --language для выбора языка (по умолчанию английский)
    parser.addoption(
        "--language", action="store", default="en",
        help="Choose language: en, ru, fr, etc."
    )


@pytest.fixture()
def browser(request):
    # Считываем значение, переданное через командную строку
    user_language = request.config.getoption("language")

    # Создаём объект настроек Chrome
    options = Options()  
    
    # Устанавливаем язык интерфейса браузера (user_language должен быть определён заранее)
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  
    
    # Запускаем Chrome с заданными опциями
    browser = webdriver.Chrome(options=options)  
    
    # Передаём объект браузера тесту. После завершения теста выполнение продолжается после yield
    yield browser  
    
    # Закрываем браузер, чтобы не оставалось открытых процессов
    browser.quit()  