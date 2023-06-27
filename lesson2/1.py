import csv
import re

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

data_main = []

with open('info_1.txt') as i1:
    data = i1.read()
    os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
    os_name_reg = re.compile(r'Название ОС:\s*\S*')
    os_code_reg = re.compile(r'Код продукта:\s*\S*')
    os_type_reg = re.compile(r'Тип системы:\s*\S*')

    os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
    os_name_list.append(os_name_reg.findall(data)[0].split()[2])
    os_code_list.append(os_code_reg.findall(data)[0].split()[2])
    os_type_list.append(os_type_reg.findall(data)[0].split()[2])

with open('info_2.txt') as i2:
    data = i2.read()
    os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
    os_name_reg = re.compile(r'Название ОС:\s*\S*')
    os_code_reg = re.compile(r'Код продукта:\s*\S*')
    os_type_reg = re.compile(r'Тип системы:\s*\S*')

    os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
    os_name_list.append(os_name_reg.findall(data)[0].split()[2])
    os_code_list.append(os_code_reg.findall(data)[0].split()[2])
    os_type_list.append(os_type_reg.findall(data)[0].split()[2])

with open('info_3.txt') as i3:
    data = i3.read()
    os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
    os_name_reg = re.compile(r'Название ОС:\s*\S*')
    os_code_reg = re.compile(r'Код продукта:\s*\S*')
    os_type_reg = re.compile(r'Тип системы:\s*\S*')

    os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
    os_name_list.append(os_name_reg.findall(data)[0].split()[2])
    os_code_list.append(os_code_reg.findall(data)[0].split()[2])
    os_type_list.append(os_type_reg.findall(data)[0].split()[2])

with open('main_data.csv', 'w') as m_d:
    F_N_WRITER = csv.writer(m_d)

    for i in range(0, len(os_name_list)):
        data_output = []
        if i == 0:
            data_output.append(f" Изготовитель системы,Название ОС,Код продукта,Тип системы")
            data_main.append(data_output)
            data_output = []
        data_output.append((f'{os_prod_list[i]},{os_name_list[i]},{os_type_list[i]},{os_code_list[i]}'))
        data_main.append(data_output)
    for row in data_main:
        F_N_WRITER.writerow(row)
