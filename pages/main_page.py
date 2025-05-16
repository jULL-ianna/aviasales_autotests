from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, browser):
        self.browser = browser
    
    def open(self):
        self.browser.get("https://www.aviasales.ru")
    
    def search_flight(self, origin, destination):
        self.browser.find_element(By.XPATH, "//input[@placeholder='Откуда']").send_keys(origin)
        self.browser.find_element(By.XPATH, "//input[@placeholder='Куда']").send_keys(destination)
        self.browser.find_element(By.XPATH, "//button[contains(text(), 'Найти билеты')]").click()
    
    def type_origin_city(self, text):
        self.browser.find_element(By.XPATH, "//input[@placeholder='Откуда']").send_keys(text)
    
    def is_search_button_enabled(self):
        return self.browser.find_element(By.XPATH, "//button[contains(text(), 'Найти билеты')]").is_enabled()
    
    def open_date_picker(self):
        self.browser.find_element(By.XPATH, "//div[contains(@class, 'trip-duration__date')]").click()
    
    def is_calendar_visible(self):
        return self.browser.find_element(By.XPATH, "//div[contains(@class, 'calendar')]").is_displayed()
