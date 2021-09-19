import sqlite3 as sq

import consts
from functions_fold import about_funcs, account_funcs, help_funcs, soulmates_search_funcs, \
    confirmation_funcs, error_funcs

bot = consts.bot
user_1 = consts.user


# Creating a users table if not exists
with sq.connect('db/users.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        reg_number INTEGER PRIMARY KEY AUTOINCREMENT,      
        user_id INTEGER,
        first_name TEXT, 
        nickname TEXT, 
        metro_dep TEXT, 
        metro_arr TEXT,
        stars INTEGER DEFAULT 0
      )''')
    con.commit()

with sq.connect('db/users.db') as con:
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS confirms (
        user_id INTEGER,
        soul_id INTEGER,
        date TEXT,
        file TEXT,
        authorized INTEGER DEFAULT 0
        )''')


def get_curr_user_1(user_id):
    global user_1

    with sq.connect('db/users.db') as con:
        cur = con.cursor()

        cur.execute('''SELECT user_id FROM users WHERE user_id=?''', (user_id,))
        pack = cur.fetchall()
        if len(pack) > 0:
            user_1.reg_status = True
            cur.execute('''SELECT first_name, nickname, metro_dep, metro_arr FROM users WHERE user_id=?''', (user_id,))
            pack = cur.fetchall()
            for i in pack:
                user_1.name = i[0]
                user_1.nickname = i[1]
                user_1.dep_code = i[2]
                user_1.arr_code = i[3]
        elif len(pack) == 0:
            user_1.reg_status = False


def listener(messages):
    global user_1
    for message in messages:
        chat_id = message.chat.id
        user_id = message.chat.id

        if message.content_type == 'text':
            new_msg = str(message.text).lower()

            # Общедоступные функции
            if new_msg in ['/help', 'помощь', '/start']:
                help_funcs.help_func(message)
            elif new_msg == '/about':
                about_funcs.about_func(message)
            elif new_msg in ['/faq', 'faq']:
                bot.send_message(chat_id, consts.faq_text)

            # В разработке
            elif new_msg == '/report':
                error_funcs.no_func_error(message)
            elif new_msg == '/review':
                error_funcs.no_func_error(message)

            # Функции, доступные только без регистрации
            elif new_msg in ['/register', 'регистрация', 'зарегистрироваться']:
                get_curr_user_1(user_id)
                if not user_1.reg_status:
                    account_funcs.get_basic_step(message)
                elif user_1.reg_status:
                    error_funcs.user_exists_error(message)

            # Функции, доступные только с регистрацией
            elif new_msg in ['/view_account', 'посмотреть профиль']:
                get_curr_user_1(user_id)
                if user_1.reg_status:
                    account_funcs.view_acc_func(message)
                elif not user_1.reg_status:
                    error_funcs.no_registration_error(message)

            elif new_msg in ['/edit_account', 'изменить аккаунт', 'редактировать профиль']:
                get_curr_user_1(user_id)
                if user_1.reg_status:
                    account_funcs.ask_what_to_edit_step(message)
                elif not user_1.reg_status:
                    error_funcs.no_registration_error(message)

            elif new_msg in ['delete_account', 'удалить профиль']:
                get_curr_user_1(user_id)
                if user_1.reg_status:
                    account_funcs.delete_account(message)
                elif not user_1.reg_status:
                    error_funcs.no_registration_error(message)

            elif new_msg in ['/souls_search', 'поиск попутчиков', 'искать попутчиков', 'найти попутчиков',
                             'найти соула', 'поиск соула', 'искать соула']:
                get_curr_user_1(user_id)
                if user_1.reg_status:
                    soulmates_search_funcs.main_find_souls(user_1, user_id, message)
                else:
                    error_funcs.no_registration_error(message)

            elif new_msg in ['/confirm', 'мы встретились']:
                get_curr_user_1(user_id)
                if user_1.reg_status:
                    confirmation_funcs.start_conf_process(message)
                elif not user_1.reg_status:
                    error_funcs.no_registration_error(message)

            elif new_msg == '/untrusted':
                get_curr_user_1(user_id)
                if user_1.reg_status:
                    confirmation_funcs.send_unapproved_num(message)
                elif not user_1.reg_status:
                    error_funcs.no_registration_error(message)

            elif new_msg in ['/trust_me', 'подтвердить встречу']:
                get_curr_user_1(user_id)
                if user_1.reg_status:
                    confirmation_funcs.approve_conf(message)
                elif not user_1.reg_status:
                    error_funcs.no_registration_error(message)

            # В разработке

            # Обработка непонятного текста
            else:
                error_funcs.ununderstandable_text(message)

        # Обработка сообщений, которые содержат не текст
        elif message.content_type != 'text':
            bot.send_message(chat_id, 'Я не умею пока обрабатывать никакие входящие сообщения, кроме текстовых, '
                                      'только если я не прошу прислать мне такой файл.')


bot.set_update_listener(listener)
bot.polling(none_stop=True, timeout=None)
