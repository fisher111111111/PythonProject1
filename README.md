
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

├── src/                
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── api /\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|──api_manager.py\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|──auth_client.py\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──health_check.py\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── data_models/\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|──project_data.py\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──project_data_akk_bookings.py\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── enums /\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|──constant_of_headers.py\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──constant_of_url.py\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── scenarios/\  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|──scenario_auth.py\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|──scenario_booking.py\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─.....\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── utils/\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|──project_data_all_validator.py\
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──project_data_validator.py\
├── tests/                
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── test_auth.py      
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── test_booking.py   
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── ...  
├── .gitignore \
├── conftest.py          \
├── README.md            \
└── requirements.txt      

### Расположение проекта
Проект расположен на удаленном репозитории на [**Github**](https://github.com/fisher111111111/Module_4_2)

### Запуск автоматизированных тестов на Python 

Для запуска тестов необходимо установить соответствующие библиотеки и зависимостей:

```bash
pip install -r requirements.txt
````

Для запуска тестов используйте следующую команду:
```bash
pytest
```
Для получения отчета в Allure Report используйте следующую команду:
```bash
allure serve allure-results
```

### Авторы
**Рыбальченко Алексей**
### Контакты
e-mail: [alexey_1979@mail.ru]()

Telegram: [@Rybalchenko_Alexei]()




