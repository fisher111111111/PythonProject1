
### Автоматизированные тесты для проверки API документации сайта [Restful-booker](https://restful-booker.herokuapp.com)

### Описание проекта
Это проект для проверки API документации сайта [Restful-booker](https://restful-booker.herokuapp.com), который 
содержит набор автоматизированных тестов для [API Restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html), написанных
на Python с использованием фреймворка `pytest` и создания отчетности в Allure Report. 
Тесты проверяют функциональность различных эндпойнтов API, включая создание токена авторизации, получение списка заказов, получение информации о заказе по ID, создание, обновление, частичное обновление и удаление заказа, получения информации о `ping` (скорости соединения) 

Проект составлен с использованием Python и его библиотек, и предназначен для обеспечения непрерывного тестирования [API Restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html) и автоматического
обнаружения регрессий. Он позволяет быстро и эффективно проверять работоспособность API после внесения 
изменений в код или данные.

С самой API документацией сайта [Restful-booker](https://restful-booker.herokuapp.com) можно ознакомиться по ссылке 
https://restful-booker.herokuapp.com/apidoc/index.html

### Структура проекта

```markdown

├── src/
│   ├── api/
│   │   ├── api_manager.py
│   │   ├── auth_client.py
│   │   └── health_check.py
│   ├── data_models/
│   │   ├── project_data.py
│   │   ├── project_data_all_bookings.py
│   │   └── project_data_patch.py
│   ├── enums/
│   │   ├── constant_of_headers.py
│   │   └── constant_of_url.py
│   ├── scenarios/
│   │   ├── scenario_auth.py
│   │   ├── scenario_booking.py
│   │   └── ...
│   └── utils/
│       ├── project_data_all_validator.py
│       ├── project_data_all_validator.py      
│       ├── project_patch_data_validator.py
│       └── urls.py
├── tests/
│   ├── test_auth.py
│   ├── test_booking.py
│   └── ...
├── .gitignore
├── conftest.py
├── README.md
└── requirements.txt
```
### Расположение проекта
Проект расположен на удаленном репозитории на [**Github**](https://github.com/fisher111111111/PythonProject1)

### Запуск автоматизированных тестов на Python 

Для установки фреймворка необходимо установить соответствующие библиотеки:

```bash
pip install -r requirements.txt
````

Для запуска тестов используйте команду:
```bash
pytest
```
Для запуска тестов с сохранением результатов в Allure используйте команду:
```bash
python -m pytest tests -v -s --alluredir=allure-results
```
Для получения отчета в Allure Report используйте команду:
```bash
allure serve allure-results
```

### Авторы
**Рыбальченко Алексей**
### Контакты
e-mail: [alexey_1979@mail.ru]()

Telegram: [@Rybalchenko_Alexei]()




