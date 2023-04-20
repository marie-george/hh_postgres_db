# hh_postgres_db
Parser of 10 good IT companies from hh.ru/Парсер 10 классых IT-компаний с сайта hh.ru

Имя базы данных - hh_postgres_db
Модуль для создания таблиц в базе данных - db_creation.py
Модуль для заполнения созданных таблиц данными - db_filling.py (данные парсятся с сайта с помощью request-функций из модуля requests_to_hh)
Модуль взаимодействия с пользователем - main.py (для вывода значений из БД используются методы из класса DBManager, модуль db_manager.py)

Список компаний, по которым парсится информация:
Yadro,
Selectel,
Рут Код,
Лига цифровой экономики,
Лаборатория наносемантика,
X5 Tech,
BI.ZONE,
Diasoft,
NGENIX,
Outlines Technologies

