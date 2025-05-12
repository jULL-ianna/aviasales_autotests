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

    @allure.story("Невалидные параметры поиска")
    def test_invalid_search_params(self):
        """Тест с некорректными параметрами (ошибка 400)"""
        invalid_params = {
            "origin": "INVALID_CODE",
            "destination": "UNKNOWN",
            "currency": "RUB"
        }
        response = requests.get(f"{API_ENDPOINT}/prices_for_dates", params=invalid_params)
        assert response.status_code == 400, "Ожидалась ошибка 400"

    @allure.story("Поиск без обязательных параметров")
    def test_missing_required_params(self):
        """Тест с отсутствующим параметром 'origin'"""
        response = requests.get(f"{API_ENDPOINT}/prices_for_dates", params={"destination": "LED"})
        assert response.status_code != 200, "API принял запрос без обязательного параметра"

    @allure.story("Граничные значения дат")
    def test_past_date_search(self):
        """Тест с прошедшей датой (должен вернуть ошибку)"""
        params = {
            "origin": "MOW",
            "destination": "LED",
            "depart_date": "2020-01-01"  # Прошедшая дата
        }
        response = requests.get(f"{API_ENDPOINT}/prices_for_dates", params=params)
        assert response.status_code == 400 or "error" in response.json()