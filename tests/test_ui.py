import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage

@pytest.mark.ui
@allure.feature("Поиск авиабилетов")
@allure.story("Проверка основного функционала поиска")
def test_valid_search(browser):
    with allure.step("Открываем главную страницу Aviasales"):
        page = MainPage(browser)
        page.open()
    
    with allure.step("Ищем рейс Москва → Стамбул"):
        page.search_flight("Москва", "Стамбул")
    
    with allure.step("Проверяем, что результаты содержат 'Стамбул'"):
        assert "Стамбул" in browser.page_source

@pytest.mark.ui
@allure.feature("Валидация формы")
def test_empty_origin_error(browser):
    with allure.step("Пытаемся отправить форму без города вылета"):
        page = MainPage(browser)
        page.open()
        page.search_flight("", "Стамбул")
    
    with allure.step("Проверяем сообщение об ошибке"):
        assert "Укажите город вылета" in browser.page_source

@pytest.mark.ui
@allure.feature("Автодополнение городов")
def test_autocomplete_city(browser):
    with allure.step("Вводим 'Моск' в поле города"):
        page = MainPage(browser)
        page.open()
        page.type_origin_city("Моск")
    
    with allure.step("Проверяем появление подсказки с Москвой"):
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Москва')]"))
        )

@pytest.mark.ui
@allure.feature("Состояние кнопки поиска")
def test_search_button_disabled(browser):
    with allure.step("Проверяем, что кнопка поиска неактивна при загрузке"):
        page = MainPage(browser)
        page.open()
        assert not page.is_search_button_enabled()

@pytest.mark.ui
@allure.feature("Календарь выбора дат")
def test_date_picker(browser):
    with allure.step("Открываем календарь дат"):
        page = MainPage(browser)
        page.open()
        page.open_date_picker()
    
    with allure.step("Проверяем видимость календаря"):
        assert page.is_calendar_visible()
