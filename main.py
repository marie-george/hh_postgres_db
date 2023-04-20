from db_manager import DBManager

print('Привет! Вы попали в базу данных 10 самых крутых IT-компаний с сайта HeadHunter (актуальность на 19.04.2023г).\nВыберите '
      "дальнейшее действие:\nВывести список всех компаний и количество вакансий у каждой компании: нажмите s\nВывести список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию: "
      "нажмите t\nВывести среднюю зарплату по вакансиям: нажмите n\nВывести список всех вакансий, у которых зарплата выше средней по всем вакансиям: нажмите g\nВывести список всех вакансий, в названии которых содержатся определенное слово (например “python”): нажмите j\nЕсли вы хотите завершить программу: "
      "нажмите z")

user_choice = input()

while user_choice != 'z':
    if user_choice == 's':
        #вывод списка всех компаний и количество вакансий у каждой компании
        dbm = DBManager()
        conn = dbm.get_connection()
        companies_and_vacancies_count = dbm.get_companies_and_vacancies_count()
        for row in companies_and_vacancies_count:
            print(row)
        user_choice = input('Введите следующую команду ')
    if user_choice == 't':
        #вывод списка всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        dbm = DBManager()
        conn = dbm.get_connection()
        all_vacancies = dbm.get_all_vacancies()
        for row in all_vacancies:
            print(row)
        user_choice = input('Введите следующую команду ')
    if user_choice == 'n':
        #вывод средней зарплаты по вакансиям
        dbm = DBManager()
        conn = dbm.get_connection()
        avg_salary = dbm.get_avg_salary()
        print(avg_salary)
        user_choice = input('Введите следующую команду ')
    if user_choice == 'g':
        #вывод списка всех вакансий, у которых зарплата выше средней по всем вакансиям
        dbm = DBManager()
        conn = dbm.get_connection()
        vacancies_with_higher_salary = dbm.get_vacancies_with_higher_salary()
        for row in vacancies_with_higher_salary:
            print(row)
        user_choice = input('Введите следующую команду ')
    if user_choice == 'j':
        #вывод списка всех вакансий, в названии которых содержится клучевое
        keyword = input('Введите ключевое слово (внимание! поиск может быть чувствителен к регистру) ')
        dbm = DBManager()
        conn = dbm.get_connection()
        vacancies_with_keyword = dbm.get_vacancies_with_keyword(keyword)
        for row in vacancies_with_keyword:
            print(row)
        user_choice = input('Введите следующую команду ')
    else:
        #обработка неверного значения, введенного пользователем
        print('Вы ввели неверное значение. Пожалуйста, попробуйте еще раз или нажмите z для завершения программы')
        user_choice = input()

print('Программа завершена')