-- получает список всех компаний и количество вакансий у каждой компании
SELECT company_name, vacancies_number FROM companies

-- получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
SELECT vacancy_name, company_name, salary, link_to_vacancy FROM vacancy INNER JOIN companies USING(company_id)

-- получает среднюю зарплату по вакансиям
SELECT AVG(salary) FROM vacancy WHERE salary != 0

-- получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
SELECT vacancy_name, salary, link_to_vacancy FROM vacancy WHERE salary > (SELECT AVG(salary) FROM vacancy WHERE salary != 0)

-- получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
SELECT vacancy_name, salary, link_to_vacancy FROM vacancy WHERE vacancy_name LIKE '%Python%'