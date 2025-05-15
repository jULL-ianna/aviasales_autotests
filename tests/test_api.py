import pytest
from api.client import AviasalesAPI

@pytest.mark.api
def test_search_tickets_status_code():
    api = AviasalesAPI()
    response = api.search_tickets("Moscow", "Istanbul")
    assert response.status_code == 200

@pytest.mark.api
def test_search_tickets_response_structure():
    api = AviasalesAPI()
    response = api.search_tickets("Moscow", "Istanbul")
    assert "tickets" in response.json()

@pytest.mark.api
def test_invalid_city_error():
    api = AviasalesAPI()
    response = api.search_tickets("InvalidCity", "Istanbul")
    assert response.status_code == 404

@pytest.mark.api
def test_get_prices():
    api = AviasalesAPI()
    response = api.get_prices("12345")
    assert response.status_code == 200

@pytest.mark.api
def test_empty_params():
    api = AviasalesAPI()
    response = api.search_tickets("", "")
    assert response.status_code == 400