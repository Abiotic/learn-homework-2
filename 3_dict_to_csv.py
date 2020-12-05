"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

employees_list = [
			        {'name': 'Anna', 'age': 25, 'job': 'Scientist'}, 
			        {'name': 'Mike', 'age': 88, 'job': 'Programmer'}, 
			        {'name': 'Hades', 'age': 666, 'job': 'Lord of evil'},
			        {'name': 'Petr the Pig', 'age': 35, 'job': 'unemployed'},
			        {'name': 'Jack', 'age': 48, 'job': 'janitor'}

			    ]

def main(employees_list):
	emp_str = ''
	with open ('list_of_employees_v1.csv','w',encoding='utf-8') as f_emp:
		header = 'name;age;job'
		f_emp.write(header + '\n')
		for employee in employees_list:
			for emp in employee.values():
				emp_str += f'{emp};'
				
			f_emp.write(emp_str[:-1] + '\n')
			emp_str = ''
			

			
#знаю, что так можно и наверное и нужно, но решила попробовать свое
		'''
		fields = ['name', 'age', 'job']
		writer = csv.DictWriter(f_emp, fields, delimiter=';')
		writer.writeheader()
		for employee in employees_list:
			writer.writerow(employee)

		'''


if __name__ == "__main__":
    main(employees_list)
