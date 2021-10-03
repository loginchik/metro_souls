import logging
import telebot
import classes
from telebot import types

# consts
with open('token.txt', 'r') as tgtoken:
    token = str(tgtoken.read())

logger = logging.getLogger('TelebotExceptionHandler')


class MyExceptionHandler(telebot.ExceptionHandler):

    def handle(self, exception):
        logger.error("Error calling API", exception)
        return True


exception_handler = MyExceptionHandler
bot = telebot.TeleBot(token=token, exception_handler=exception_handler)
user = classes.User(None)

# texts
about_text = 'Metro Soulmates — это бот, разработанный небольшой командой студенток, которые хотели облегчить ' \
             'и разнообразить себе и другим таким же студентам жизнь. \n\nДля чего нужен бот? Ответ прост: чтобы ' \
             'искать попутчиков — таких же студентов — и ездить на учебу и с нее вместе.' \
             '\n\nИнстаграм проекта - @metro.soulmates'

# ------ Account functions ------

# account registration
acc_create_conf_text = 'Регистрация прошла успешно, теперь вы можете полноценно пользоваться ботом!' \
                       '\n\n{0}\n{1}\n\n{2}\n{3}'.format('/help',
                                                         '/faq',
                                                         '/viewaccount',
                                                         '/soulssearch')

dep_ask_text = 'Как называется станция отправления?'
arr_ask_text = 'Как называется станция прибытия?'

few_stations_warning_first_text = 'Станция с таким названием есть на нескольких разных линиях. ' \
                                  'Сейчас я пришлю схему с номерами, цветами и названиями линий метро'
few_stations_warning_second_text = 'Если станция, которую вы имеете в виду, находится на одной из линий ' \
                                   'метро, напишите номер этой линии (не название или цвет, а именно номер). ' \
                                   'Если станция находится на МДЦ 1, то напишите "МЦД 1"; ' \
                                   'если на МЦД 2 — "МЦД 2"'

acc_exists_text = 'Вы уже создавали профиль, повторная регистрация невозможна \n\n{0}\n{1}'.format('/viewaccount',
                                                                                                   '/help')

what_to_change_text = 'Что вы хотите изменить? \n\nВозможные варианты ответа (без кавычек): ' \
                      '"{0}", "{1}", "{2}", "{3}"'.format('имя',
                                                          'никнейм',
                                                          'станция отправления',
                                                          'станция прибытия')

nick_update_text = 'Сейчас обновлю ваш ник из данных телеграма'
new_name_text = 'Пожалуйста, напишите новое имя'
new_dep_text = 'Новая станция отправления?'
new_arr_text = 'Новая станция прибытия?'

# delete account
acc_del_conf_text = 'Ваш аккаунт успешно удален. Если захотите еще раз воспользоваться ботом, ' \
                    'не забудьте зарегистрироваться снова, запустив команду {0}'.format('/register')
goodbye_text = 'Надеемся, наш бот был для вас полезен! \n\nЕсли у вас есть какие-то комментарии или желание оставить ' \
               'отзыв, вы можете написать его разработчику (@loginchik) или в директ нашего инстаграма: ' \
               'metro.soulmates.'
do_not_delete_acc_text = 'Это хорошо, что вы решили остаться. Аккаунт сохранен в базе пользователей'
delete_acc_confirm_ask_text = 'Вы уверены, что хотите удалить аккаунт? После удаления аккаунта восстановить данные, ' \
                              'которые к нему привязаны, будет невозможно\n\n- Да\n- Нет)'

# ------ Soulmates text ------

no_souls_found_text = "К сожалению, ваш соул еще не зарегистрировался"

conf_success_text = 'Отчет о встрече успешно записан, спасибо большое за информацию!\n\n' \
                    'Если вы еще раз захотите встретиться с тем же человеком, вы можете записать отчет еще раз — ' \
                    'это не запрещено и, наоборот, порадует тех, кто работает над проектом.'
ask_for_conf_text = 'Пришлите доказательство. \n\nИм может быть аудио, видео или фото, ' \
                    'на котором слышно или видно вас двоих'
ask_for_soul_nick = 'Пришлите ник того, с кем вы встретились. Ник должен начинаться с @!'
no_unapproved_text = 'У вас нет неподтвержденных встреч'

conf_not_suitable_format_text = 'Кажется, вы прислали не тот формат(('

# ------ Errors ------

no_func_text = 'К сожалению, эта функция еще разрабатывается и недоступна в данный момент'

no_station_error_text = 'Ошибка регистрации: станции с таким названием нет в базе данных.' \
                        '\n\nНачните регистрацию заново.'

no_registration_error_text = 'Ваш аккаунт не найден в базе данных, функция недоступна'

not_text_text = 'В ответ ожидалось текстовое сообщение, а получено нечто иное. К сожалению, функция прекратилась. ' \
                'Вы можете попробовать запустить ее заново'

ununderstandable_text_text = 'Не удалось распознать никакую команду. Возможно, вы требуете невозможного ' \
                             'или ошиблись в написании запроса'

any_error_text = 'К сожалению, произошла системная ошибка'

few_ways_no_station_text = 'Станция под таким названием не найдена на этом пути. ' \
                           'Процесс регистрации остановлен, попробуйте заново'

not_nick_text = 'Это не похоже на ник пользователя... Процесс остановлен, попробуйте заново'

soul_is_not_reg_text = 'Похоже, что ваш соул не зарегистрирован в боте. ' \
                       'Попросите его сделать это и попробуйте отправить отчет заново'

# ---- Stickers -----
sad_sticker = 'CAACAgIAAxkBAAEC7aBhRl4U7rzGDaMoAWDhP1f3AutOOgACaBEAAkAwiUtLxBKN7HrbtiAE'
error_sticker = 'CAACAgIAAxkBAAEC7YxhRlfXHvsef8cgeKq8wiEhRnGjKgACqg0AAuODiUjd0_CDy4ej6yAE'

# ----- Keyboard Markups -----

# Edit account buttons
edit_account_markup = types.ReplyKeyboardMarkup()
edit_account_markup.one_time_keyboard = True

edit_name_btn = types.KeyboardButton(text='Имя')
update_nickname_btn = types.KeyboardButton(text='Никнейм')
edit_dep_btn = types.KeyboardButton(text='Станция прибытия')
edit_arr_btn = types.KeyboardButton(text='Станция отправления')

edit_account_markup.row(edit_name_btn, update_nickname_btn)
edit_account_markup.row(edit_dep_btn, edit_arr_btn)

# New user markup
not_registered_markup = types.ReplyKeyboardMarkup()

register_btn = types.KeyboardButton(text='Регистрация')
help_btn = types.KeyboardButton(text='Помощь')
faq_btn = types.KeyboardButton(text='FAQ')

not_registered_markup.row(register_btn)
not_registered_markup.row(help_btn, faq_btn)

# Basic markup
basic_markup = types.ReplyKeyboardMarkup()
