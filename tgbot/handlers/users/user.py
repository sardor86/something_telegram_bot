from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards import url_channel
from tgbot.models import Channels, Videos


async def user_start(message: Message):
    linked = True

    all_channels = await Channels().get_all_channel()

    for channel in all_channels:
        user_channel_status = await message.bot.get_chat_member(chat_id=channel.channel, user_id=message.from_user.id)
        if user_channel_status["status"] == 'left':
            linked = False
    if linked:
        await message.reply('ВЫ ПОДПИСАНЫ МОЛОДЕЦ')

        video = await Videos().get_video()

        await message.bot.send_video(message.from_user.id, video.video)
    else:
        await message.reply('НЕ ПОДПИСАН ХОЛОДЕЦ',
                            reply_markup=await url_channel())


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
