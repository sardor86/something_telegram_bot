from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import CallbackQuery, Message

from tgbot.misc import AddChannel
from tgbot.models import Channels


async def start_add_chanel(callback: CallbackQuery) -> None:
    await callback.message.edit_text('Отправте нам сылку на канал')

    await AddChannel.get_channel_url.set()


async def get_chanel_url(message: Message, state: FSMContext) -> None:
    if await Channels().add_channel(message.text):
        await message.reply('Успешно добавлено')
        await state.finish()
        return None
    await message.reply('Этот канал уже существует')


def register_add_chanel_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_add_chanel,
                                       lambda callback: callback.data == 'add_chanel')
    dp.register_message_handler(get_chanel_url,
                                state=AddChannel.get_channel_url)
