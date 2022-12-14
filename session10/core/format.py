FORMATS = [
    {  # по-хорошему задать массив через точное определние структуры с помощью классов, но пока я не пробовал классы в питоне
        'formatDataDelimeter': '\\n',  # разделитель между форматами хранения
        'userDataDelimeter': ';',  # разделитель данных пользователей
        'userPropertiesDelimeter': ',',  # разделитель свойств пользователя

        # Пример входного файла с данными:
        'example': "\n;,Фамилия_1,,Имя_1,,Телефон_1,,Описание_1,;;,Фамилия_2,,Имя_2,,Телефон_2,,Описание_2,;\n"
    },
    {
        'formatDataDelimeter': '&',
        'userDataDelimeter': ';',
        'userPropertiesDelimeter': ',',

        # пример входного файла с данными:
        'example': "&;,Фамилия_1,,Имя_1,,Телефон_1,,Описание_1,;;,Фамилия_2,,Имя_2,,Телефон_2,,Описание_2,;&"
    },
    {
        'formatDataDelimeter': '%',
        'userDataDelimeter': ';',
        'userPropertiesDelimeter': ',',

        # пример входного файла с данными:
        'example': "%;,Фамилия_1,,Имя_1,,Телефон_1,,Описание_1,;;,Фамилия_2,,Имя_2,,Телефон_2,,Описание_2,;%"
    }

    #     пример входного файла с данными:
    #     "\n;,Фамилия_1,,Имя_1,,Телефон_1,,Описание_1,;;,Фамилия_2,,Имя_2,,Телефон_2,,Описание_2,;\n&;,Фамилия_1,,Имя_1,,Телефон_1,,Описание_1,;;,Фамилия_2,,Имя_2,,Телефон_2,,Описание_2,;&%;,Фамилия_1,,Имя_1,,Телефон_1,,Описание_1,;;,Фамилия_2,,Имя_2,,Телефон_2,,Описание_2,;%"
]