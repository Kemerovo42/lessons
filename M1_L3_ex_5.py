import telebot
from pass_gen import gen_password
from coin_drop import drop_coin
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8499634467:AAFqep3BfbglLwCORwtmW4iEMoVYh6R1oLc")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    gen_password(10)
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['passwword'])
def send_password(message):
    password = gen_password(8)
    bot.reply_to(message, "Ваш пароль:",password)

@bot.message_handler(commands=['coin'])
def send_password(message):
    coin = drop_coin()
    bot.reply_to(message, "Сторона монетки:",coin)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
