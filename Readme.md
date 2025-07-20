
### Автоматизированные тесты для проверки API документации сайта [Restful-booker](https://restful-booker.herokuapp.com)

### Описание проекта
Это проект для проверки API документации сайта [Restful-booker](https://restful-booker.herokuapp.com), который 
содержит набор автоматизированных тестов для [API Restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html), написанных
на Python с использованием фреймворка `pytest` и библиотек `requests`. 
Тесты проверяют функциональность различных эндпойнтов API, включая создание токена авторизации, получение списка заказов, получение информации о заказе по ID, создание, обновление, частичное обновление и удаление заказа, получения информации о `ping` (скорости соединения) 

Проект составлен с использованием Python и его библиотек, и предназначен для обеспечения непрерывного тестирования [API Restful-booker](https://restful-booker.herokuapp.com/apidoc/index.html) и автоматического
обнаружения регрессий. Он позволяет быстро и эффективно проверять работоспособность API после внесения 
изменений в код или данные.

С самой API документацией сайта [Restful-booker](https://restful-booker.herokuapp.com) можно ознакомиться по ссылке 
https://restful-booker.herokuapp.com/apidoc/index.html

### Структура проекта

├── README.md            \
├── constant.py          \
├── conftest.py          \
├── src/                
│        ├── api.py    
│        ├── data_models.py    
│        ├── scenarios.py  
│        ├── utils.py    
├── tests/                
│        ├── test_auth.py      
│        ├── test_booking.py   
│        └── ...              
└── requirements.txt      

### Расположение проекта
Проект расположен на удаленном репозитории на [**Github**](https://github.com/fisher111111111/Module_4_2)

### Запуск автоматизированных тестов на Python 

Для запуска тестов необходимо установить соответствующие библиотеки:

```bash
pip install -r requirements.txt
````

Для запуска тестов используйте следующую команду:
```bash
pytest
```
### Авторы
**Рыбальченко Алексей**
### Контакты
e-mail: [alexey_1979@mail.ru]()

Telegram: [@Rybalchenko_Alexei]()




