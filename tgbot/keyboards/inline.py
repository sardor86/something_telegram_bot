from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)

    keyboard.insert(InlineKeyboardButton('Создать видео', callback_data='create_video'))
    keyboard.insert(InlineKeyboardButton('Удалить видео', callback_data='delete_video'))
    keyboard.insert(InlineKeyboardButton('Добавить канал', callback_data='add_chanel'))

    return keyboard
