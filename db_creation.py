import psycopg2

from config import config

params = config()

#создание подключения к базе данных postgres
conn = psycopg2.connect(database="postgres", **params)

# Создание базы данных hh_postgres_db
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE hh_postgres_db")
cur.close()
conn.close()

#создание подключения к базе данных hh_postgres_db
conn = psycopg2.connect(database="hh_postgres_db", **params)

try:
    with conn:
        with conn.cursor() as cur:
            # Создание таблиц companies и vacancy в базе данных hh_postgres_db
            cur.execute("CREATE TABLE companies (company_id int PRIMARY KEY, company_name varchar, vacancies_number int)")
            cur.execute("CREATE TABLE vacancy (vacancy_id int PRIMARY KEY, company_id int, vacancy_name varchar(200), "
                        "salary int, link_to_vacancy varchar, area varchar, experience varchar, employment varchar)")
finally:
    conn.close()
