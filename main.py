import telebot as t
bot=t.TeleBot('8328347131:AAFz-1Evk2zevDhKaM92DMN5_Vi1swYIfvk')


@bot.message_gandler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'ДАРОУ,чо')


bot.polling(nont_stop=1)