import requests


def get_company_id(companies):
    """Получает id компаний, список названий которых передан в функцию"""
    id_list = []
    for i in companies:
        response = requests.get(f"https://api.hh.ru/employers?text={i}").json()
        company_id = response['items'][0]['id']
        id_list.append(company_id)
    return id_list


def get_vacancies_link(ids):
    """Получает единую ссылку на все вакансии компаний, список id которых передан в функцию"""
    vacancies_link_list = []
    for i in ids:
        id_response = requests.get(f"https://api.hh.ru/employers/{i}").json()
        vacancies_url = id_response['vacancies_url']
        vacancies_link_list.append(vacancies_url)
    return vacancies_link_list


def get_vacancies_number(links):
    """Получает количество вакансий, опубликованных каждой компанией, из списка ссылок, переданных в функцию"""
    vacancies_number_list = []
    for i in links:
        vacancies_response = requests.get(f"{i}", params={'per_page': '100', 'page': 0}).json()
        vacancies_number = 0
        for n in vacancies_response['items']:
            vacancies_number += 1
        vacancies_number_list.append(vacancies_number)
    return vacancies_number_list


def get_salary(salary_info: dict):
    """Обработка поля salary(зарплата): предпочтительно выводить зарплату 'от', если же она не указана,
    то выводить зарплату 'до'. Или выводить 0, если поле отсутствует"""
    if salary_info:
        if salary_info.get('to'):
            return salary_info['to']
        if salary_info.get('from'):
            return salary_info['from']
    return 0


def get_vacancy_info(links):
    """Полчает данные по вакансиям, опубликованных каждой компанией, из списка ссылок, переданных в функцию"""
    vacancies_info_list = []
    for i in links:
        vacancies_response = requests.get(f"{i}", params={'per_page': '100', 'page': 0}).json()
        for vacancy in vacancies_response['items']:
            vacancies_info_list.append({
                "vacancy_id": vacancy['id'],
                "company_id": vacancy['employer']['id'],
                "vacancy_name": vacancy['name'],
                "salary": get_salary(vacancy['salary']),
                "link": vacancy['alternate_url'],
                "area": vacancy['area']['name'],
                "experience": vacancy['experience']['name'],
                "employment": vacancy['employment']['name']
            })
    return vacancies_info_list
