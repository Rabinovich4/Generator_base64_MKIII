import json
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from new_values import get_random_int, get_random_string

from parsing_json import parsing_contragen_json, parsing_user_json

# Начало окна ткинтера
root = Tk()
root.title('Generator_base64 MkIII')
root.geometry('500x500')

# Инициализация режима блокнота
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Вкладка с контрагентом
kontragent_tab = ttk.Frame(notebook)
notebook.add(kontragent_tab, text='Контрагент')

label = Label(kontragent_tab, text='Введите ИНН')
label.pack()
entry_inn = ttk.Entry(kontragent_tab)
entry_inn.pack()

label = Label(kontragent_tab, text='Введите КПП')
label.pack()
entry_kpp = ttk.Entry(kontragent_tab)
entry_kpp.pack()

label = Label(kontragent_tab, text='Введите ОГРН')
label.pack()
entry_ogrn = ttk.Entry(kontragent_tab)
entry_ogrn.pack()

label = Label(kontragent_tab, text='Введите Полное наименование организации')
label.pack()
entry_full_name = ttk.Entry(kontragent_tab)
entry_full_name.pack()

label = Label(kontragent_tab, text='Введите esiaOid')
label.pack()
entry_esia_oid = ttk.Entry(kontragent_tab)
entry_esia_oid.pack()

label = Label(kontragent_tab, text='Введите bidderCode')
label.pack()
entry_bidder_code = ttk.Entry(kontragent_tab)
entry_bidder_code.pack()

label = Label(kontragent_tab, text='Введите objectId')
label.pack()
entry_object_id = ttk.Entry(kontragent_tab)
entry_object_id.pack()


class ContragentParams:
    def __init__(self):
        self.root = parsing_contragen_json()

    def get_inn(self):
        input_inn = entry_inn.get()
        if input_inn == '':
            input_inn = get_random_int(9)
        else:
            input_inn = int(input_inn)
        return input_inn

    def get_kpp(self):
        input_kpp = entry_kpp.get()
        if input_kpp == '':
            input_kpp = get_random_int(9)
        else:
            input_kpp = int(input_kpp)
        return input_kpp

    def get_ogrn(self):
        input_ogrn = entry_ogrn.get()
        if input_ogrn == '':
            input_ogrn = get_random_int(13)
        else:
            input_ogrn = int(input_ogrn)
        return input_ogrn

    def get_full_name(self):
        input_full_name = entry_full_name.get()
        if input_full_name == '':
            input_full_name = str(parsing_contragen_json()['data']['structuredObject']['bidder']['legal']['fullName'])
        else:
            input_full_name = input_full_name
        return input_full_name

    def get_object_id(self):
        input_object_id = entry_object_id.get()
        if input_object_id == '':
            input_object_id = get_random_int(9)
        else:
            input_object_id = int(input_object_id)
        return input_object_id

    def get_bidder_code(self):
        input_bidder_code = entry_bidder_code.get()
        if input_bidder_code == '':
            input_bidder_code = get_random_int(9)
        else:
            input_bidder_code = int(input_bidder_code)
        return input_bidder_code

    def get_esia_oid(self):
        input_esia_oid = entry_esia_oid.get()
        if input_esia_oid == '':
            input_esia_oid = get_random_int(9)
        else:
            input_esia_oid = int(input_esia_oid)
        return input_esia_oid

    def refactor_contragent_data(self):
        # Получение json пакета контрагента
        data_contragent_json = parsing_contragen_json()

        # Получение значения полного наименования организации и разделение на Гис/номер
        full_name = self.get_full_name()
        name_part = full_name.split()[0]  # Предполагается, что "Гис" - это первое слово
        number_part = ''.join(filter(str.isdigit, full_name))
        new_number = int(number_part) + 1 if number_part else 1
        new_full_name = f"{name_part} {new_number}"

        # Замена целевых значений
        data_contragent_json['data']['structuredObject']['bidder']['legal']['esiaOid'] = get_random_int(9)
        data_contragent_json['index']['objectId'] = get_random_int(9)
        data_contragent_json['data']['structuredObject']['bidder']['commonInfo']['bidderCode'] = get_random_int(9)
        data_contragent_json['data']['structuredObject']['bidder']['legal']['inn'] = str(self.get_inn())
        data_contragent_json['data']['structuredObject']['bidder']['legal']['kpp'] = str(self.get_kpp())
        data_contragent_json['data']['structuredObject']['bidder']['legal']['ogrn'] = str(self.get_ogrn())

        # Установка нового значения имени/мыла контрагента "Имя №"
        data_contragent_json['data']['structuredObject']['bidder']['legal']['fullName'] = new_full_name
        data_contragent_json['data']['structuredObject']['bidder']['contactInfo']['email'] = f"gis-elkkkkk{new_number}@mailforspam.com"

        # Выбор директории для сохранения файла
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data_contragent_json, json_file, ensure_ascii=False, indent=4)
        # Перезапись внутри
        file_path = 'contragent.json'
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_contragent_json, json_file, ensure_ascii=False, indent=4)


# Создаем экземпляр класса ContragentParams
contragent_params_data = ContragentParams()

# Привязываем метод refactor_contragent_data к кнопке
btn_generate_contragent = ttk.Button(kontragent_tab, text='Сгенерировать',
                                     command=contragent_params_data.refactor_contragent_data)
btn_generate_contragent.pack()

# Вкладка с юзером
user_tab = ttk.Frame(notebook)
notebook.add(user_tab, text='Юзер')

label = Label(user_tab, text='Введите Фамилию')
label.pack()
entry_last_name = ttk.Entry(user_tab)
entry_last_name.pack()

label = Label(user_tab, text='Введите Имя')
label.pack()
entry_first_name = ttk.Entry(user_tab)
entry_first_name.pack()

label = Label(user_tab, text='Введите Отчество')
label.pack()
entry_middle_name = ttk.Entry(user_tab)
entry_middle_name.pack()


class UserParams:
    def __init__(self):
        self.root = parsing_contragen_json()
        self.root = parsing_user_json()

    def get_last_name(self):
        input_last_name = entry_last_name.get()
        if input_last_name == '':
            input_last_name = get_random_string(9)
        else:
            input_last_name = str(input_last_name)
        return input_last_name

    def get_first_name(self):
        input_first_name = entry_first_name.get()
        if input_first_name == '':
            input_first_name = get_random_string(9)
        else:
            input_first_name = str(input_first_name)
        return input_first_name

    def get_middle_name(self):
        input_middle_name = entry_middle_name.get()
        if input_middle_name == '':
            input_middle_name = get_random_string(9)
        else:
            input_middle_name = str(input_middle_name)
        return input_middle_name

    def refactor_user_data(self):
        data_contragent_json = parsing_contragen_json()
        data_user_json = parsing_user_json()

        new_bidder_code = data_contragent_json['data']['structuredObject']['bidder']['commonInfo']['bidderCode']
        data_user_json['data']['structuredObject']['bidderUser']['bidderInfo']['bidderCode'] = new_bidder_code
        new_esia_oid = data_contragent_json['data']['structuredObject']['bidder']['legal']['esiaOid']
        data_user_json['data']['structuredObject']['bidderUser']['bidderInfo']['esiaOid'] = new_esia_oid
        data_user_json['index']['objectId'] = get_random_int(9)
        data_user_json['data']['structuredObject']['bidderUser']['commonInfo']['userId'] = get_random_int(9)
        data_user_json['data']['structuredObject']['bidderUser']['commonInfo']['prnOid'] = get_random_int(9)
        data_user_json['data']['structuredObject']['bidderUser']['personInfo']['FIO']['lastName'] = get_random_string(5)
        data_user_json['data']['structuredObject']['bidderUser']['personInfo']['FIO']['firstName'] = get_random_string(5)
        data_user_json['data']['structuredObject']['bidderUser']['personInfo']['FIO']['middleName'] = get_random_string(5)

        # Выбор директории для сохранения файла
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data_user_json, json_file, ensure_ascii=False, indent=4)
        # Перезапись внутри
        file_path = 'user.json'
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_user_json, json_file, ensure_ascii=False, indent=4)


# Создаем экземпляр класса UserParams
user_params_data = UserParams()

# Привязываем метод chek к кнопке
btn_generate_user = ttk.Button(user_tab, text='Сгенерировать',
                               command=user_params_data.refactor_user_data)
btn_generate_user.pack()

# Конец окна ткинтера
root.mainloop()