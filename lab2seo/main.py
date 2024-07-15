import telebot
from telebot import types
import random

bot = telebot.TeleBot('6935115893:AAHE8LuXjNvQkOYg9LZ4EiDkHV-v6NIQn_o')


start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_button = types.KeyboardButton("Начать")
start_markup.add(start_button)

topic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
health_button = types.KeyboardButton("Моделирование")
sports_button = types.KeyboardButton("Организация ЭВМ и систем")
work_button = types.KeyboardButton("Базы данных")
entertainment_button = types.KeyboardButton("Архитектура операционных систем")
topic_markup.row(health_button, sports_button)
topic_markup.row(work_button, entertainment_button)

model_questions = [
    {
        'question': 'характеристика,указывающая важность сообщения т.е. его приоритет.',
        'options': ['Место сообщения', 'Длина сообщения', 'Тип сообщения'],
        'correct_option': 2,
    },
    {
        'question': 'характеристика, определяющая размер сообщения.',
        'options': ['Место сообщения', 'Длина сообщения', 'Тип сообщения'],
        'correct_option': 1,
    },
    {
        'question': 'характеристика,указывающая адрес устройства, для которого оно предназначено.',
        'options': ['Место сообщения', 'Длина сообщения', 'Тип сообщения'],
        'correct_option': 0,
    },
    {
        'question': 'Может  ли быть случайная величина одновременно и дискретной и непрерывной?',
        'options': ['да', 'не знаю', 'нет'],
        'correct_option': 2,
    },
    {
        'question': 'Каков "физический" смысл математического ожидания и дисперсии?',
        'options': ['Математическое ожидание - это среднее значение случайной величины, а дисперсия - это мера разброса значений вокруг среднего.',
                    'Математическое ожидание - это вероятность наступления конкретного события, а дисперсия - это мера неопределенности и случайности.',
                    'Математическое ожидание - это среднеквадратичное отклонение, а дисперсия - это мера ожидаемого количества событий.'],
        'correct_option': 0,
    },
]
evm_questions = [
    {
        'question': 'Что понимается под процессором данных?',
        'options': ['функциональное устройство, работающее как интерпретатор команд', 'функциональное устройство, работающее как преобразователь данных, в соответствии с арифметическими операциями', 'запоминающее устройство, в котором хранятся данные и команды, пересылаемые между процессорами'],
        'correct_option': 1,
    },
    {
        'question': 'Векторная (или матричная) обработка предполагает:',
        'options': ['обработку одной командой нескольких комплектов операндов', 'обработку одной командой одного комплекта операндов', 'обработку несколькими командами одного комплекта операндов'],
        'correct_option': 2,
    },
    {
        'question': 'Для больших ЭВМ размер слова составляет:',
        'options': ['4 байта', '2 байта', '1 байта'],
        'correct_option': 0,
    },
    {
        'question': 'К каким носителям информации относятся DVD?',
        'options': ['к магнитным', 'к магнитооптическим', 'к оптическим'],
        'correct_option': 2,
    },
    {
        'question': 'К адресным регистрам исполнительного блока микропроцессора относится:',
        'options': ['BX', 'SP', 'CX'],
        'correct_option': 1,
    },
]
DB_questions = [
    {
        'question': 'Плоская таблица, состоящая из столбцов и строк в реляционной теории, называется:',
        'options': ['доменом', 'кортежем', 'отношением'],
        'correct_option': 2,
    },
    {
        'question': 'Тип данных SMALLINT в SQL — это:',
        'options': ['вещественное число', '"короткое целое" число', 'символьная строка'],
        'correct_option': 1,
    },
    {
        'question': 'Структура данных, в которой каждый объект может иметь более одного господствующего узла, называется:',
        'options': ['сетевой моделью', 'списком', 'реляционной моделью'],
        'correct_option': 0,
    },
    {
        'question': 'Откат транзакции в SQL осуществляется командой?',
        'options': ['COMMIT', 'REVOKE', 'ROLLBACK'],
        'correct_option': 2,
    },
    {
        'question': 'Инструмент для определения характеристик и структуры данных называется:',
        'options': ['DDL', 'языком определения данных', 'языком управления данными'],
        'correct_option': 1,
    },
]
OS_questions = [
    {
        'question': 'Смысл виртуальной памяти заключается в том, что ...',
        'options': ['память процессу выделяется сегментами', 'все процессы выполняются в едином адресном пространстве', 'каждый процесс выполняется в собственном виртуальном адресном пространстве'],
        'correct_option': 2,
    },
    {
        'question': 'В UNIX функции драйверов принтеров выполняют:',
        'options': ['фильтры печати', 'системные вызовы', 'специальные файлы устройств'],
        'correct_option': 0,
    },
    {
        'question': 'Подсистема STREAMS в UNIX предоставляет:',
        'options': ['интерфейс обмена данными, основанный на сообщениях', 'набор различных услуг ядра прикладным процессам', 'интерфейс обмена данными, основанный на сокетах'],
        'correct_option': 0,
    },
    {
        'question': 'В UNIX для того, чтобы удалить некоторый файл из каталога, нужно иметь право на:',
        'options': ['запись для каталога', 'выполнение для файла', 'выполнение для каталога'],
        'correct_option': 0,
    },
    {
        'question': 'В UNIX для небуферизированного обмена данными с устройством используются:',
        'options': ['именованный канал', 'символьные файлы устройств',
                    'порты ввода-вывода'],
        'correct_option': 1,
    },
]

# Create a dictionary to keep track of the user's progress for each topic.
user_progress = {}
user_scores = {}


@bot.message_handler(func=lambda message: message.text in ['Моделирование', 'Организация ЭВМ и систем', 'Базы данных', 'Архитектура операционных систем'])

def handle_topic(message):
    user_id = message.from_user.id
    topic = message.text

    # Устанавливаем прогресс пользователя для выбранной темы на 0.
    user_progress[user_id] = {'topic': topic, 'question_index': 0}
    user_scores[user_id] = 0
    bot.send_message(message.chat.id, f'Вы выбрали тему: {topic}')

    if topic == "Моделирование":

        random.shuffle(model_questions)
        send_next_question(user_id, message.chat.id)
    elif topic == "Организация ЭВМ и систем":
        random.shuffle(evm_questions)
        send_next_question(user_id, message.chat.id)
    elif topic == "Базы данных":
        random.shuffle(DB_questions)
        send_next_question(user_id, message.chat.id)
    elif topic == "Архитектура операционных систем":
        random.shuffle(OS_questions)
        send_next_question(user_id, message.chat.id)


def send_next_question(user_id, chat_id):
    user_data = user_progress.get(user_id)
    if user_data:
        topic = user_data['topic']
        question_index = user_data['question_index']

        if topic == "Моделирование" and question_index < len(model_questions):
            question = model_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)

        elif topic == "Организация ЭВМ и систем" and question_index < len(evm_questions):
            question = evm_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)
        # Добавьте аналогичные условия для других тем (Работа и Развлечения)
        elif topic == "Базы данных" and question_index < len(DB_questions):
            question = DB_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)

        elif topic == "Архитектура операционных систем" and question_index < len(OS_questions):
            question = OS_questions[question_index]
            bot.send_message(chat_id, question['question'])
            options = question['options']
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for option in options:
                markup.add(types.KeyboardButton(option))

            bot.send_message(chat_id, "Выберите вариант ответа:", reply_markup=markup)

        else:
            display_results(user_id, chat_id)
            # Добавляем кнопку для возврата к выбору тем после завершения вопросов.
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(types.KeyboardButton("Вернуться к темам"))
            bot.send_message(chat_id, "Вы ответили на все вопросы в данной теме.", reply_markup=markup)
    else:
        bot.send_message(chat_id, "Произошла ошибка. Пожалуйста, выберите тему снова.")


@bot.message_handler(
    func=lambda message: message.text in ['обслуживания потока заявок', 'оптимизации решений, специально приспособленных к «многошаговым» операциям', 'конфликтных ситуаций', 'ASSEMBLE', 'REPORT', 'TABULATE',
                                                           'эскизного проекта', 'рабочего проекта', 'научно-исследовательской работы', 'гибридной', 'интегральной', 'последовательной',
                                                           'все вероятности состояний как функции времени', 'вероятности конечных состояний как функции времени', 'вероятности конечных состояний как функции переходов',
                                                           'функциональное устройство, работающее как интерпретатор команд', 'функциональное устройство, работающее как преобразователь данных, в соответствии с арифметическими операциями', 'запоминающее устройство, в котором хранятся данные и команды, пересылаемые между процессорами',
                                                           'обработку одной командой нескольких комплектов операндов', 'обработку одной командой одного комплекта операндов', 'обработку несколькими командами одного комплекта операндов',
                                                           '4 байта', '2 байта', '1 байта', 'к магнитным', 'к магнитооптическим', 'к оптическим', 'BX', 'SP', 'CX',
                                                           'доменом', 'кортежем', 'да', 'не знаю', 'нет', 'Математическое ожидание - это среднее значение случайной величины, а дисперсия - это мера разброса значений вокруг среднего.',
                    'Математическое ожидание - это вероятность наступления конкретного события, а дисперсия - это мера неопределенности и случайности.',
                    'Математическое ожидание - это среднеквадратичное отклонение, а дисперсия - это мера ожидаемого количества событий.', 'отношением', 'вещественное число', '"короткое целое" число', 'символьная строка', 'сетевой моделью', 'списком', 'реляционной моделью',
                                                           'COMMIT', 'REVOKE', 'ROLLBACK', 'DDL', 'языком определения данных', 'языком управления данными', 'память процессу выделяется сегментами', 'все процессы выполняются в едином адресном пространстве', 'каждый процесс выполняется в собственном виртуальном адресном пространстве',
                                                           'фильтры печати', 'системные вызовы', 'специальные файлы устройств', 'интерфейс обмена данными, основанный на сообщениях', 'набор различных услуг ядра прикладным процессам', 'интерфейс обмена данными, основанный на сокетах',
                                                           'запись для каталога', 'Место сообщения', 'Длина сообщения', 'Тип сообщения', 'выполнение для файла', 'выполнение для каталога', 'именованный канал', 'символьные файлы устройств', 'порты ввода-вывода'])
def handle_answer(message):
    user_id = message.from_user.id
    user_data = user_progress.get(user_id)

    if user_data:
        topic = user_data['topic']
        question_index = user_data['question_index']

        if topic == "Моделирование" and question_index < len(model_questions):
            question = model_questions[question_index]
        elif topic == "Организация ЭВМ и систем" and question_index < len(evm_questions):
            question = evm_questions[question_index]
        elif topic == "Базы данных" and question_index < len(DB_questions):
            question = DB_questions[question_index]
        elif topic == "Архитектура операционных систем" and question_index < len(OS_questions):
            question = OS_questions[question_index]
        else:
            bot.send_message(message.chat.id, "Произошла ошибка. Пожалуйста, выберите тему снова.")
            return

        correct_option = question['correct_option']

        if message.text == question['options'][correct_option]:
            bot.send_message(message.chat.id, "Правильный ответ!")
            user_scores[user_id] += 1  # Увеличиваем баллы пользователя на 1
        else:
            bot.send_message(message.chat.id, "Неправильный ответ!")

        # Increment the question index and send the next question.
        user_progress[user_id]['question_index'] += 1
        send_next_question(user_id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Произошла ошибка. Пожалуйста, выберите тему снова.")


def display_results(user_id, chat_id):
    if user_id in user_scores:
        score = user_scores[user_id]
        bot.send_message(chat_id, f'Ваш результат: {score} баллов')
        del user_scores[user_id]  # Удалите баллы пользователя после отображения результата


@bot.message_handler(func=lambda message: message.text == "Вернуться к темам")
def return_to_topics(message):
    user_id = message.from_user.id
    if user_id in user_progress:
        del user_progress[user_id]
    bot.send_message(message.chat.id, "Вы вернулись к выбору тем.", reply_markup=topic_markup)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}, выберите тему:'
    bot.send_message(message.chat.id, mess, reply_markup=topic_markup)


@bot.message_handler(func=lambda message: message.text in ['Моделирование', 'Организация ЭВМ и систем', 'Базы данных', 'Архитектура операционных систем'])
def handle_topic(message):
    bot.send_message(message.chat.id, f'Вы выбрали тему: {message.text}')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hello", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я не знаю о чем ты", parse_mode='html')




bot.polling(none_stop=True)

