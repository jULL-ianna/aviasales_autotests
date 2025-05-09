# aviasales_autotests

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
