import telebot as t
from telebot import types
bot=t.TeleBot('8245955171:AAHMPGTSCBNHTs-KhEDv8kgWbwQcS-9smm4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1=(types.KeyboardButton('Информация о боте🤖'))
    btn2 = (types.KeyboardButton('Навигация🧭'))
    btn3 = (types.KeyboardButton('Справки📑'))
    markup.row(btn1,btn2,btn3)
    bot.send_message(message.chat.id,'Что вас интересует?', reply_markup=markup)
    bot.register_next_step_handler(message,on_click)

#---------------------------------------------------------
#Основная логика
def on_click(message):
    if message.text=='Навигация🧭':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Навигационная карта🗺'))
        btn2 = (types.KeyboardButton('Переход в корпус🏢'))
        btn3 = (types.KeyboardButton('Туалет🧻'))
        btn4 = (types.KeyboardButton('Общепиты рядом☕️'))
        markup.add(btn1, btn2).add(btn3,btn4)
        bot.send_message(message.chat.id, 'Что вы ищете?', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)

    elif message.text=='Информация о боте🤖':
        information(message)
    elif message.text=='/start':
        start(message)
    elif message.text=='Вернуться обратно':
        start(message)

    elif message.text=='Справки📑':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        btn2 = (types.KeyboardButton('Как заказать справку в ИСУ📄'))
        btn3 = (types.KeyboardButton('Cправка для военкомата🪖'))
        markup.add(btn1).row(btn2,btn3)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, 'Отлично! Давай я помогу тебе разобраться со справками!', reply_markup=markup)


#-------------общепит--
    elif message.text=='Навигационная карта🗺':
        navig(message)
    elif message.text == 'Общепиты рядом☕️':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id,
                         'DonerБери\n'
                         'Адрес: Айская ул., 82 (этаж 1)\n'
                         'Телефон: +7 (917) 009-20-23\n'
                         'Официальные сайты: vk.com/donerberi_ufa\n'
                         '\n'
                         'Баракат-1\n'
                         'Адрес: Верхнеторговая площадь, 6\n'
                         'Телефон:+7 (917) 462-45-78\n'
                         'Официальные сайты: https://vk.com/barakatcafe\n'
                         'Студентам делают скидку!\n'
                         '\n'
                         'Баракат-2\n'
                         'Адрес: ул. Ленина, 26\n'
                         'Телефон:\n'
                         '+7 (917) 462-45-78\n'
                         'Официальные сайты: https://vk.com/barakatcafe\n'
                         'Студентам делают скидку!\n'
                         '\n'
                         'Айбат Халляр\n'
                         'Адрес: ул. Свердлова, 100\n'
                         'Телефон: +7 (927) 951-77-73  /  +7 (927) 951-77-73\n'
                         'Официальные сайты: --\n'
                         '\n'
                         'Рахат\n'
                         'Адрес: ул. Мустая Карима, 3, корп. 2этаж 1\n'
                         'Телефон: +7 (987) 254-44-93\n'
                         'Официальные сайты: --\n'
                         'Студентам делают скидку!\n'
                         '\n'
                         'Union Coffee Rec\n'
                         'Адрес: ул. Пушкина, 86, Уфа\n'
                         'Телефон: +7 (987) 033-13-86\n'
                         'Официальные сайты: https://vk.com/public213219200\n'
                         '\n'
                         'Кунак\n'
                         'Адрес: Коммунистическая ул., 50\n'
                         'Телефон: +7 (917) 734-97-37\n'
                         'Официальные сайты: https://vk.com/kunak_halal', reply_markup=markup)
    elif message.text=='Переход в корпус🏢':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('2 корпус'))
        btn2 = (types.KeyboardButton('3 корпус'))
        btn3 = (types.KeyboardButton('6 корпус'))
        btn4 = (types.KeyboardButton('7 корпус'))
        btn5 = (types.KeyboardButton('8 корпус'))
        btn6 = (types.KeyboardButton('9 корпус'))
        btn7 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, 'Выберите корпус, в который вы хотите перейти', reply_markup=markup)
    elif message.text=='Туалет🧻':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('1'))
        btn2 = (types.KeyboardButton('2'))
        btn3 = (types.KeyboardButton('3'))
        btn4 = (types.KeyboardButton('4'))
        btn5 = (types.KeyboardButton('5'))
        btn6 = (types.KeyboardButton('6'))
        btn7 = (types.KeyboardButton('7'))
        btn8 = (types.KeyboardButton('8'))
        btn9 = (types.KeyboardButton('9'))
        btn10 = (types.KeyboardButton('Вернуться обратно'))
        markup.add(btn1,btn2,btn3,btn4).row(btn5,btn6,btn7,btn8).row(btn9,btn10)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, 'Выберите корпус', reply_markup=markup)

    elif message.text == '2 корпус':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            'Переход из 1 корпуса - При входе в 1 корпус, поверните Направо, там будет лестница, поднимитесь на 2 этаж, влево до конца коридора.))', reply_markup=markup)
    elif message.text == '3 корпус':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            'Переход из 2 корпуса - При входе в 2 корпус, впереди лестница, поднимитесь на 3 этаж, справа от лестницы длинный коридор, идите до конца.', reply_markup=markup)
    elif message.text == '6 корпус':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            'Переход из 6 корпуса - У входа со стороны вахты стоит дверь, за ней - подземный переход в 7 корпус\n'
            'Переход из 2 корпуса - При входе в 2 корпус, впереди лестница, поднимитесь на 2 этаж, влево до конца коридора.))', reply_markup=markup)
    elif message.text == '7 корпус':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            'Переход из 6 корпуса - У входа со стороны вахты стоит дверь, за ней - подземный переход в 7 корпус))', reply_markup=markup)
    elif message.text == '8 корпус':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
        'Переход из 1 корпуса - При входе в 1 корпус, поверните налево, там будет лестница, поднимитесь на 2 этаж, далее идити вправо до конца, там будет развилка в 7 и 9 корпуса, по указателю на стене - идите влево))',
        reply_markup=markup)
    elif message.text == '9 корпус':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            'Переход из 1 корпуса - При входе в 1 корпус, поверните налево, там будет лестница, поднимитесь на 2 этаж, далее идити вправо до конца, там будет развилка в 7 и 9 корпуса, по указателю на стене - идите вправо\n'
            'Переход из 8 корпуса - При входе в 8 корпус, поверните налево, там будет лестница, поднимитесь на 2 этаж, право до конца коридора))', reply_markup=markup)


    elif message.text == '1':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.add(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
        '1-1 женский слева и справа от входа\n1-2 мужской женский в левой части корпуса\n1-3 мужской женский в левой части корпуса\n1-4 женский в левой части корпуса', reply_markup=markup)
    elif message.text == '2':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.add(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
        '2-1 мужской напротив входа по прямой\n2-2 женский в правой части корпуса, около лестницы\n2-4 женский в правой части корпуса, около лестницы', reply_markup=markup)
    elif message.text == '3':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
        '3-2 женский Возле викторины ПИШ\n3-3 мужской Возле банкомата', reply_markup=markup)
    elif message.text == '4':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
        '4-2 женский ПИШ рядом с Путиным', reply_markup=markup)
    elif message.text == '5':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
        '5-2 женский', reply_markup=markup)
    elif message.text == '6':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            '6-1 мужской возле лестницы\n6-2 женский у лестницы', reply_markup=markup)
    elif message.text == '7':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            '7-1 мужской женский(слева от лестницы)\n7-2 мужской женский(слева от лестницы)\n7-3 мужской женский', reply_markup=markup)
    elif message.text == '8':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
            '8-1 мужской женский\n8-2 мужской возле буфета', reply_markup=markup)
    elif message.text == '9':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, \
    '9-1 женский Возле 901\n9-2 мужской(Возле 902) женский\n9-3 мужской женский Возле 306\n9-4 мужской женский\n9-5 мужской женский', reply_markup=markup)



    elif message.text=='Как заказать справку в ИСУ📄':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id,'Алгоритм заказа справок с места обучения в "ИСУ УУНиТ:\n1) Открыть isu.uust.ru и войти в систему, используя свой логин и пароль\n'
'2) В боковом меню открыть раздел «Заявки» -«МФСО»-«Ваши заявки»\n'
'3) Нажать кнопку (Добавить заявку) обязательно заполняем все графы нажать кнопку «Создать»\n'
'4) Проверить внесенные данные и нажать кнопку «Обновить» (при необходимости)\n'
'5) ОБЯЗАТЕЛЬНО нажать на ЗЕЛЁНУЮ кнопку «Отправить на согласование»\n'
'6) В раскрывшемся окне нажать на КРАСНУЮ кнопку «Отправить на согласование»\n'
'7) Отслеживать статус* заявки и ожидать уведомления о готовности\n'
'8) Забрать готовую справку по адресу: г. Уфа, ул. К. Маркса, д. 12, к. 7, каб. 109А (МФСО)\n'
'ВАЖНО: если Вам необходимо получить НЕСКОЛЬКО справок, то необходимо отправить НЕСКОЛЬКО ЗАЯВОК\n'
'*Статусы заявок могут быть:\n'
'«ЗАЯВКА ПРИНЯТА» - заявка, которая еще не отправлена на согласование и не принята в работу.\n'
'«ОТПРАВЛЕНО НА СОГЛАСОВАНИЕ» - заявка, находящаяся на согласовании в МФСО.\n'
'«ПЕЧАТЬ ДОКУМЕНТА» - заявка принята в работу.\n'
'«МОЖНО ЗАБИРАТЬ» - документ готов и подготовлен к выдаче.', reply_markup=markup)
    elif message.text=='Cправка для военкомата🪖':
        markup = types.ReplyKeyboardMarkup()
        btn1 = (types.KeyboardButton('Вернуться обратно'))
        markup.row(btn1)
        bot.register_next_step_handler(message, on_click)
        bot.send_message(message.chat.id, '1) Справку для военкомата делают в 7-212(7 корпус 212 кабинет - мобилизационный отдел)\n'
                         '2) При себе иметь паспорт, приписаное свидетельство, аттестат о среднем общем образовании, 1 фотография 3*4, при наличии - водительское удостоверение\n'
                        '3) Перед входом в мобилизационный отдел, на двери будет висеть бумага с информацией о том, какой факультет к какому окошку подходит, находите свой факультет и идётё в соответствующее окно\n'
                        '4) Предоставляете все необходимые документы\n'
                        '5) Вам оформляют заявку.\n''\n'
                         'ДОПОЛНИТЕЛЬНО:\n''\n'
                         'Если вы забыли какой-либо документ (например аттестат), вы можете открыть госуслуги и предоставить данные оттуда\n'
                         'Вопрос: «Нельзя ли обойтись полной справкой об обучении?»\n'
                         'Ответ: «Нет, в военкомат нужна специальная справка, которую делают лишь в мобилизационном отделе.»\n'
                         'Вопрос: «Через сколько дней будет готова справка?»\n'
                         'Ответ: «Примерно через 5 дней она будет готова»\n'
                         'Вопрос: «А что, если её не сделать?»\n'
                         'Ответ: «У вас будут проблемы, вам это не нужно»\n', reply_markup=markup)
#----------------------------------

def information(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = (types.KeyboardButton('Вернуться обратно'))
    markup.row(btn1)

    file = open('robo-gif.gif', 'rb')
    bot.send_message(message.chat.id, 'Привет!👋 Я СтудГид, бот-помощник для студентов УУНиТ! Я постараюсь помочь тебе с тем, с чем смогу!\nКак перейти в другой корпус, как заказать и получить справку, да даже туалет как найти - подскажу😜! Вернись обратно и выбери подходящий раздел😉!\n'
                                      'Если у вас есть предложения по проекту, или же вы нашли баг, писать сюда -->\n'
                                      '@siftdnv', reply_markup=markup)
    bot.send_animation(message.chat.id, file)
    bot.register_next_step_handler(message, on_click)
def navig(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = (types.KeyboardButton('Вернуться обратно'))
    markup.row(btn1)

    file = open('karta.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id,
    'Отправляю Вам навигационную карту УУНиТ!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
@bot.message_handler()
def info(message):
    if message.text.lower()=='привет':
        if message.from_user.last_name==None:
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
        else:
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')
    else:
        bot.send_message(message.chat.id, 'Извините, я пока не знаю такой команды! Нажмите /start , чтобы вернуться(')
bot.polling(none_stop=True)