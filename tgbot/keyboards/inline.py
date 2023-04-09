from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.models import Channels


def admin_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('Создать видео', callback_data='create_video'))
    keyboard.insert(InlineKeyboardButton('Удалить видео', callback_data='delete_video'))
    keyboard.insert(InlineKeyboardButton('Добавить канал', callback_data='add_chanel'))
    keyboard.insert(InlineKeyboardButton('Удалить канал', callback_data='delete_chanel'))

    return keyboard


async def url_channel() -> InlineKeyboardMarkup:
    all_channel = await Channels().get_all_channel()

    keyboard = InlineKeyboardMarkup(row_width=1)

    for channel in all_channel:
        keyboard.insert(InlineKeyboardButton('ПОДПИСАТСЯ', url='https://t.me/' + channel.channel[1:]))

    return keyboard
