from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.aviasales.ru"

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Откуда']"))
        )

    def search_flight(self, origin, destination):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Откуда']").send_keys(origin)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Куда']").send_keys(destination)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Найти билеты')]").click()