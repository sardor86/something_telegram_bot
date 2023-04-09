from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards import admin_menu


async def admin_start(message: Message):
    await message.reply("menu",
                        reply_markup=admin_menu())


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["menu"], state="*", is_admin=True)
