import psycopg2


class DBManager():

    def get_connection(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="hh_postgres_db",
            user="postgres",
            password="latino87Aruba@"
        )
        return self.conn

    def get_companies_and_vacancies_count(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT company_name, vacancies_number FROM companies")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()

    def get_all_vacancies(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT vacancy_name, company_name, salary, link_to_vacancy FROM vacancy INNER JOIN companies USING(company_id)")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()

    def get_avg_salary(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT AVG(salary) FROM vacancy WHERE salary != 0")
                    average = cur.fetchall()
                    return average
        finally:
            self.conn.close()

    def get_vacancies_with_higher_salary(self):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute("SELECT vacancy_name, salary, link_to_vacancy FROM vacancy WHERE salary > (SELECT AVG(salary) FROM vacancy WHERE salary != 0)")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()

    def get_vacancies_with_keyword(self, keyword):
        try:
            with self.conn:
                with self.conn.cursor() as cur:
                    cur.execute(f"SELECT vacancy_name, salary, link_to_vacancy FROM vacancy WHERE vacancy_name LIKE '%{keyword}%'")
                    rows = cur.fetchall()
                    return rows
        finally:
            self.conn.close()

