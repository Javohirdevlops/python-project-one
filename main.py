from translate import transletori
import  telebot
TOKEN = "5016588177:AAHIOU_2zeOi4tDVTNGflQ-tVkMmQVEZ_48"
tarjimon_bot = telebot.TeleBot(token=TOKEN)
@tarjimon_bot.message_handler( commands = [ 'start' ])
def salom(message):
    xabar = "Assalomu alaykum, tarjimon botiga xush kelibsiz."
    xabar+="\nMAtiningizni yuboring."
    tarjimon_bot.reply_to(message,xabar.title())

@tarjimon_bot.message_handler(fuct=lambda msg:  msg.text is not None)

def tarjimon(message):

    msg = message.text

    tarjimon_bot.reply_to( message, transletori ( msg ) )

#Bot Ishga tushdi

tarjimon_bot.polling()