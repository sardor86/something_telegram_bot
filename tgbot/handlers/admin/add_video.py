from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import CallbackQuery, Message

from tgbot.misc import AddVideo
from tgbot.models import Videos


async def start_crate_video(callback: CallbackQuery) -> None:
    await callback.message.edit_text('Отправте нам видео')

    await AddVideo.get_video.set()


async def get_video(message: Message, state: FSMContext) -> None:
    video = message.video.file_id

    id_video = await Videos().add_video(video)
    await message.reply('Видео сохранено')
    await message.reply(f'id видео {id_video}')
    await state.finish()


async def get_not_video(message: Message) -> None:
    await message.reply('Это не видео')

    return None


def register_add_video_handler(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(start_crate_video,
                                       lambda callback: callback.data == 'create_video')

    dp.register_message_handler(get_video,
                                content_types=['video'],
                                state=AddVideo.get_video)

    dp.register_message_handler(get_not_video,
                                lambda message: not message.video,
                                state=AddVideo.get_video)

