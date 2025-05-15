import pytest
from pages.main_page import MainPage

@pytest.mark.ui
def test_valid_search(driver):
    page = MainPage(driver)
    page.open()
    page.search_flight("Москва", "Стамбул")
    assert "Стамбул" in driver.page_source

@pytest.mark.ui
def test_empty_origin_error(driver):
    page = MainPage(driver)
    page.open()
    page.search_flight("", "Стамбул")
    assert "Укажите город вылета" in driver.page_source

@pytest.mark.ui
def test_autocomplete_city(driver):
    page = MainPage(driver)
    page.open()
    city_input = driver.find_element(By.XPATH, "//input[@placeholder='Откуда']")
    city_input.send_keys("Моск")
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Москва')]"))
    )

@pytest.mark.ui
def test_search_button_disabled(driver):
    page = MainPage(driver)
    page.open()
    assert not driver.find_element(By.XPATH, "//button[contains(text(), 'Найти билеты')]").is_enabled()

@pytest.mark.ui
def test_date_picker(driver):
    page = MainPage(driver)
    page.open()
    driver.find_element(By.XPATH, "//div[contains(@class, 'trip-duration__date')]").click()
    assert driver.find_element(By.XPATH, "//div[contains(@class, 'calendar')]").is_displayed()