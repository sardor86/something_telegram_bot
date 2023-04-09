from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import CallbackQuery, Message

from tgbot.misc import DeleteChannel
from tgbot.models import Channels


async def start_delete_channel(callback: CallbackQuery) -> None:
    await callback.message.edit_text('Отправте нам id канала')

    await DeleteChannel.get_channel_id.set()


async def get_id_channel(message: Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        await message.reply('Это не id')

    if await Channels().delete_chanel(int(message.text)):
        await message.reply('Канал удален')
        await state.finish()
        return None
    await message.reply('Канал не удален')
    return None


def register_delete_channel_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_delete_channel,
                                       lambda callback: callback.data == 'delete_chanel')

    dp.register_message_handler(get_id_channel,
                                state=DeleteChannel.get_channel_id)
