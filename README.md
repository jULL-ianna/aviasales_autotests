# aviasales_autotests
# Финальный проект по ручному тестированию:
# https://butter-cornucopia-dbd.notion.site/e3a1714b37a1485fa6f8d5dc18dd8055

## Дипломный проект: Автоматизация тестирования Aviasales

### Запуск тестов
1. Установите зависимости:
```bash
pip install -r requirements.txt
Запустите тесты:

bash
pytest tests/ --alluredir=./allure-results
Просмотрите отчёт:

bash
allure serve ./allure-results
