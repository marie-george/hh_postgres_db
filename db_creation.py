import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="hh_postgres_db",
    user="postgres",
    password="latino87Aruba@"
)

try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE companies (company_id int PRIMARY KEY, company_name varchar, vacancies_number int)")
            cur.execute("CREATE TABLE vacancy (vacancy_id int PRIMARY KEY, company_id int, vacancy_name varchar(200), "
                        "salary int, link_to_vacancy varchar, area varchar, experience varchar, employment varchar)")
finally:
    conn.close()
