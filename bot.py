import telebot
import parser

TOKEN = "1285513700:AAHIUhXpDI6KA1PBdiWkfqfnfyTx1L7DzLM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()