import allure
import requests
import pytest
from config.settings import API_ENDPOINT

@allure.feature("API Тесты Aviasales")
class TestAviasalesAPI:
    @allure.story("Проверка доступности API")
    def test_api_availability(self):
        """Тест доступности API сервера"""
        with allure.step("Отправка HEAD-запроса"):
            response = requests.head(API_ENDPOINT, timeout=10)
        assert response.status_code in [200, 404], "API недоступен"

    @allure.story("Поиск билетов")
    @pytest.mark.xfail(reason="Требуется реальный API-ключ")
    def test_search_flights(self):
        """Тест поиска авиабилетов (пример с заглушкой)"""
        test_params = {
            "origin": "MOW",
            "destination": "LED",
            "currency": "RUB"
        }
        with allure.step("Отправка тестового запроса"):
            response = requests.get(f"{API_ENDPOINT}/prices_for_dates", params=test_params)
        
        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert isinstance(response.json(), dict)