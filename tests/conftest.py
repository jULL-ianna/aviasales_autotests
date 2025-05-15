from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Глобальное неявное ожидание
    yield driver
    driver.quit()