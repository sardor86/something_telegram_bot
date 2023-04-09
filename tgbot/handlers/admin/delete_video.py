from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import CallbackQuery, Message

from tgbot.misc import DeleteVideo
from tgbot.models import Videos


async def start_delete_video(callback: CallbackQuery) -> None:
    await callback.message.edit_text('Отправте нам id видео')

    await DeleteVideo.get_id_video.set()


async def get_id_video(message: Message, state: FSMContext) -> None:
    if not message.text.isdigit():
        await message.reply('Это не id')

    if await Videos().delete_video(int(message.text)):
        await message.reply('Видео удалено')
        await state.finish()
        return None
    await message.reply('Видео не удалена')
    return None


def register_delete_video_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_delete_video,
                                       lambda callback: callback.data == 'delete_video')
    dp.register_message_handler(get_id_video,
                                state=DeleteVideo)
