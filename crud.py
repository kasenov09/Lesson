'''
Вам нужно реализовать функционал CRUD курса. 

При создании курса Пользователь должен заполнить следующие поля:

- Категория - ограничить выбор категории из следующих:
    - Веб-разработка
    - Разработка мобильных приложений
    - Разработка игр
- Подкатегория - ограничить выбор подкатегории из следующих:
    - Python
    - JavaScript
    - Java
- Заголовок курса (максимум 60 символов)
- Описание к курсу (минимум 10 слов)
- Уровень - ограничить выбор уровня из следующих:
    - начальный
    - средний
    - профессиональный
- Цена курса  - все суммы конвертировать в сомы
    - валюта
    - сумма
'''

categories = [
    'веб-разработка',
    'разработка мобильных приложений',
    'разработка игр'
]

subcategories = [
    'python',
    'javaScript',
    'java'
]

levels = [
    'начальный',
    'средний',
    'профессиональный'
]
id = 0
def get_id():
    def inner():
        global id
        id += 1
    inner()
    return id


db = {
    get_id(): {
        'category': 'веб-разработка',
        'subcategory': 'python',
        'level': 'начальный',
        'tilte': 'Веб-разработка для начинающих',
        'description': 'Эффективные модели и практики организации профориентационной и научно-исследовательской работы с детьми с применением современных технологий',
        'price': {'currency': 'сом', 'sum': 5000}
    }
}

def get_courses():
    return db

def get_course(id: int) -> dict:
    course = db.get(id)
    if course:
        return course
    else:
        raise Exception('Такого курса нет')
    

# Create Read Update Delete
def validate_date(data):
    if data['id']:
            print ('gggggg')

def create_course():
    new_course = {
        get_id(): {
            'category': input(f'Выберите категорию {categories}: '),
            'subcategory': input(f'Выберите подкатегорию {subcategories}: '),
            'level': input(f'Выберите уровень курса {levels}: '),
            'title': input('Введите название курса: '),
            'description': input('Введите описание курса: '),
            'price': {'currency': input('Выберите валюту (cом/dollar): '), 'sum': float(input('Введите стоимость курса: '))}
        }
    }

    # print(new_course)
    # if new_course['id']['categoryh'] 


# create_course()
