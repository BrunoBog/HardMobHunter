import configparser
import gettext
import telegram
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater

# Configuring bot
from BotTelegram.model.setings import settings_handler, get_language_handler

config = configparser.ConfigParser()
config.read_file(open('config.ini'))


# Connecting to Telegram API
# Updater retrieves information and dispatcher connects commands
# classe que vai olhar se houve alguma modificação no BOT
updater = Updater(token=config['DEFAULT']['token'])

dispatcher = updater.dispatcher


def start(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    # Welcome message
    msg = "E aew ! o/\n"
    msg += "Eu Sou o  {0} e vim aqui pra te ajudar a ser um Comprador  menos compulsivo.\n".format(me.first_name)
    msg += "o que você quer fazer :?\n\n"
    msg += "/support - Opens a new support ticket\n"
    msg += "/settings - Settings of your account\n\n"
    msg += "/rastrear - Rastrear alguma encomenda\n\n"
    msg += "/buscar - Buscar promoções de um produto\n\n"

    # Commands menu
    main_menu_keyboard = [
        [telegram.KeyboardButton('/support')],
        [telegram.KeyboardButton('/settings')],
        [telegram.KeyboardButton('/rastrear')],
        [telegram.KeyboardButton('/buscar')]
    ]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)


def support(bot, update):
    """
        Sends the support message. Some kind of "How can I help you?".
    """
    bot.send_message(chat_id=update.message.chat_id,
                     text="Please, tell me what you need support with :)")


def unknown(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """
    msg = "Desculpa, não entendi o que você me falou BRO."
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


# pasta de traduções
# https://juliarizza.wordpress.com/2016/08/06/fazendo-um-bot-para-telegram-em-python/
def support_message(bot, update):
    """
        Receives a message from the user.

        If the message is a reply to the user, the bot speaks with the user
        sending the message content. If the message is a request from the user,
        the bot forwards the message to the support group.
    """
    if update.message.reply_to_message and \
       update.message.reply_to_message.forward_from:
        # If it is a reply to the user, the bot replies the user
        bot.send_message(chat_id=update.message.reply_to_message
                         .forward_from.id,
                         text=update.message.text)
    else:
        # If it is a request from the user, the bot forwards the message
        # to the group
        bot.forward_message(chat_id=int(config['DEFAULT']['support_chat_id']),
                            from_chat_id=update.message.chat_id,
                            message_id=update.message.message_id)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Give me some time to think. Soon I will return to you with an answer.")

    # Config the translations
    lang_pt = gettext.translation("pt_BR", localedir="locale", languages=["pt_BR"])

    def _(msg):
        return msg

# implementações dos methodos
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

support_handler = CommandHandler('support', support)
dispatcher.add_handler(support_handler)

unknown_handler = MessageHandler([Filters.command], unknown)
dispatcher.add_handler(unknown_handler)

dispatcher.add_handler(settings_handler)
dispatcher.add_handler(get_language_handler)




#deixar sempre por ultimo... é o Handler padrão
support_msg_handler = MessageHandler([Filters.text], support_message)
# Message handler must be the last one
dispatcher.add_handler(support_msg_handler)

while (1):
    updater.start_polling()