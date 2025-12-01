import telebot
import time
bot=telebot.TeleBot('8328347131:AAFz-1Evk2zevDhKaM92DMN5_Vi1swYIfvk')


@bot.message_handler(commands=['start'])
def main(message):
    a=10
    bot.send_message(message.chat.id,'ДАРОУ,'+message.from_user.first_name)
    while a:
        bot.send_message(message.chat.id, 'У ТЕБЯ ОСТАЛОСЬ '+str(a)+' СЕКУНД')
        time.sleep(1)
        a-=1
        if a==1:
            break
    bot.send_message(message.chat.id,'ТЫ ПРОШЕЛ испытание...')
    time.sleep(5)
    bot.send_message(message.chat.id, 'ИЛИ НЕТ?!')
    time.sleep(2)
bot.polling(none_stop=True)