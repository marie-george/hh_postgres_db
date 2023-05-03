import psycopg2

from requests_to_hh import *

from config import config

#Список компаний, по которым парсится информация
companies_list = [
    'Yadro',
    'Selectel',
    'Рут Код',
    'Лига цифровой экономики',
    'Лаборатория наносемантика',
    'X5 Tech',
    'BI.ZONE',
    'Diasoft',
    'NGENIX',
    'Outlines Technologies'
]

id_list = get_company_id(companies_list)
vacancies_link_list = get_vacancies_link(id_list)
vacancies_number_list = get_vacancies_number(vacancies_link_list)

keys = ['id', 'name', 'link', 'vacancies_number']

zipped = zip(id_list, companies_list, vacancies_link_list, vacancies_number_list)

companies_dict_list = [dict(zip(keys, values)) for values in zipped]

vacancies_info_list = get_vacancy_info(vacancies_link_list)

#создание подключения к базе данных hh_postgres_db
params = config()
conn = psycopg2.connect(database="hh_postgres_db", **params)

#заполнение таблиц базы hh_postgres_db данными, полученными с hh.ru
try:
    with conn:
        with conn.cursor() as cur:
            for i in companies_dict_list:
                cur.execute("INSERT INTO companies VALUES (%s, %s, %s)", (i['id'], i['name'], i['vacancies_number']))
            for a in vacancies_info_list:
                cur.execute("INSERT INTO vacancy VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (a['vacancy_id'],
                                                                                            a['company_id'],
                                                                                            a['vacancy_name'],
                                                                                            a['salary'], a['link'],
                                                                                            a['area'],
                                                                                            a['experience'],
                                                                                            a['employment']))

finally:
    conn.close()

