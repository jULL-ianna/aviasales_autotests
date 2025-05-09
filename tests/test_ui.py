import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import BASE_URL, TEST_CITIES

class Locators:
    """Актуальные локаторы для Aviasales"""
    COOKIE_ACCEPT = (By.ID, "cookie-accept")
    GOOGLE_BUTTON = (By.CSS_SELECTOR, "button[data-qa='auth-button']")
    FROM_INPUT = (By.CSS_SELECTOR, "input[data-qa='search-input']")
    SUGGESTION_ITEM = (By.CSS_SELECTOR, "div[data-qa='suggestion-item']")
    WEEKEND_BUTTON = (By.XPATH, "//button[contains(text(), 'Куда-нибудь')]")

@allure.feature("UI Тесты Aviasales")
class TestAviasalesUI:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Подготовка перед каждым тестом"""
        browser.get(BASE_URL)
        try:
            WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable(Locators.COOKIE_ACCEPT)).click()
        except:
            pass

    @allure.story("Авторизация")
    def test_auth_button(self, browser):
        """Проверка кнопки авторизации"""
        with allure.step("Поиск кнопки авторизации"):
            btn = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(Locators.GOOGLE_BUTTON))
            
        with allure.step("Проверка отображения"):
            assert btn.is_displayed()
            assert "Войти" in btn.text

    @allure.story("Поиск билетов")
    @pytest.mark.parametrize("city", TEST_CITIES)
    def test_city_search(self, browser, city):
        """Параметризованный тест поиска городов"""
        with allure.step(f"Ввод города {city}"):
            input_field = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(Locators.FROM_INPUT))
            input_field.clear()
            input_field.send_keys(city[:3])  # Вводим первые 3 буквы
            
        with allure.step("Проверка подсказок"):
            suggestions = WebDriverWait(browser, 5).until(
                EC.presence_of_all_elements_located(Locators.SUGGESTION_ITEM))
            assert len(suggestions) > 0, "Нет подсказок"