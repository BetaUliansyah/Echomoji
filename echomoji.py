#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram import Emoji
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import configparser

from future.utils import bytes_to_native_str as n

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

class EmojiKoe(object):
    LETTER_A = n(b'\xF0\x9F\x87\xA6')
    LETTER_B = n(b'\xF0\x9F\x87\xA7')
    LETTER_C = n(b'\xF0\x9F\x87\xA8')
    LETTER_D = n(b'\xF0\x9F\x87\xA9')
    LETTER_E = n(b'\xF0\x9F\x87\xAA')
    LETTER_F = n(b'\xF0\x9F\x87\xAB')
    LETTER_G = n(b'\xF0\x9F\x87\xAC')
    LETTER_H = n(b'\xF0\x9F\x87\xAD')
    LETTER_I = n(b'\xF0\x9F\x87\xAE')
    LETTER_J = n(b'\xF0\x9F\x87\xAF')
    LETTER_K = n(b'\xF0\x9F\x87\xB0')
    LETTER_L = n(b'\xF0\x9F\x87\xB1')
    LETTER_M = n(b'\xF0\x9F\x87\xB2')
    LETTER_N = n(b'\xF0\x9F\x87\xB3')
    LETTER_O = n(b'\xF0\x9F\x87\xB4')
    LETTER_P = n(b'\xF0\x9F\x87\xB5')
    LETTER_Q = n(b'\xF0\x9F\x87\xB6')
    LETTER_R = n(b'\xF0\x9F\x87\xB7')
    LETTER_S = n(b'\xF0\x9F\x87\xB8')
    LETTER_T = n(b'\xF0\x9F\x87\xB9')
    LETTER_U = n(b'\xF0\x9F\x87\xBA')
    LETTER_V = n(b'\xF0\x9F\x87\xBB')
    LETTER_W = n(b'\xF0\x9F\x87\xBC')
    LETTER_X = n(b'\xF0\x9F\x87\xBD')
    LETTER_Y = n(b'\xF0\x9F\x87\xBE')
    LETTER_Z = n(b'\xF0\x9F\x87\xBF')

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi! Just type anything you want, Echomoji Bot will convert your text to Emoji based alphabets and numbers.\n\nCreated by @BetaUli')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    #bot.sendMessage(update.message.chat_id, text=update.message.text)
    bot.sendMessage(update.message.chat_id, text=convert_to_emoji(update.message.text))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def convert_to_emoji(number):
    y = str(number)
    result = []
    for i in xrange(0, len(y)):
        x = y[i]
        if x == "1":
            result.append(Emoji.DIGIT_ONE_PLUS_COMBINING_ENCLOSING_KEYCAP) #1\u20e3
        elif x == "2":
            result.append(Emoji.DIGIT_TWO_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "3":
            result.append(Emoji.DIGIT_THREE_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "4":
            result.append(Emoji.DIGIT_FOUR_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "5":
            result.append(Emoji.DIGIT_FIVE_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "6":
            result.append(Emoji.DIGIT_SIX_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "7":
            result.append(Emoji.DIGIT_SEVEN_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "8":
            result.append(Emoji.DIGIT_EIGHT_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "9":
            result.append(Emoji.DIGIT_NINE_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "0":
            result.append(Emoji.DIGIT_ZERO_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "a" or x == "A":
            result.append(EmojiKoe.LETTER_A)
            result.append(" ")
        elif x == "b" or x == "B":
            result.append(EmojiKoe.LETTER_B)
            result.append(" ")
        elif x == "c" or x == "C":
            result.append(EmojiKoe.LETTER_C)
            result.append(" ")
        elif x == "d" or x == "D":
            result.append(EmojiKoe.LETTER_D)
            result.append(" ")
        elif x == "e" or x == "E":
            result.append(EmojiKoe.LETTER_E)
            result.append(" ")
        elif x == "f" or x == "F":
            result.append(EmojiKoe.LETTER_F)
            result.append(" ")
        elif x == "g" or x == "G":
            result.append(EmojiKoe.LETTER_G)
            result.append(" ")
        elif x == "h" or x == "H":
            result.append(EmojiKoe.LETTER_H)
            result.append(" ")
        elif x == "i" or x == "I":
            result.append(EmojiKoe.LETTER_I)
            result.append(" ")
        elif x == "j" or x == "J":
            result.append(EmojiKoe.LETTER_J)
            result.append(" ")
        elif x == "k" or x == "K":
            result.append(EmojiKoe.LETTER_K)
            result.append(" ")
        elif x == "l" or x == "L":
            result.append(EmojiKoe.LETTER_L)
            result.append(" ")
        elif x == "m" or x == "M":
            result.append(EmojiKoe.LETTER_M)
            result.append(" ")
        elif x == "n" or x == "N":
            result.append(EmojiKoe.LETTER_N)
            result.append(" ")
        elif x == "o" or x == "O":
            result.append(EmojiKoe.LETTER_O)
            result.append(" ")
        elif x == "p" or x == "P":
            result.append(EmojiKoe.LETTER_P)
            result.append(" ")
        elif x == "q" or x == "Q":
            result.append(EmojiKoe.LETTER_Q)
            result.append(" ")
        elif x == "r" or x == "R":
            result.append(EmojiKoe.LETTER_R)
            result.append(" ")
        elif x == "s" or x == "S":
            result.append(EmojiKoe.LETTER_S)
            result.append(" ")
        elif x == "t" or x == "T":
            result.append(EmojiKoe.LETTER_T)
            result.append(" ")
        elif x == "u" or x == "U":
            result.append(EmojiKoe.LETTER_U)
            result.append(" ")
        elif x == "v" or x == "V":
            result.append(EmojiKoe.LETTER_V)
            result.append(" ")
        elif x == "w" or x == "W":
            result.append(EmojiKoe.LETTER_W)
            result.append(" ")
        elif x == "x" or x == "X":
            result.append(EmojiKoe.LETTER_X)
            result.append(" ")
        elif x == "y" or x == "Y":
            result.append(EmojiKoe.LETTER_Y)
            result.append(" ")
        elif x == "z" or x == "Z":
            result.append(EmojiKoe.LETTER_Z)
            result.append(" ")
        else:
            result.append(x)
    return ''.join(result)



def main():
    # Create the EventHandler and pass it your bot's token.
    mytoken = open('echomoji.token', 'r').read().strip()
    print mytoken
    updater = Updater(mytoken)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
