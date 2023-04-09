from aiogram.dispatcher.filters.state import StatesGroup, State


class AddVideo(StatesGroup):
    get_video = State()


class DeleteVideo(StatesGroup):
    get_id_video = State()


class AddChannel(StatesGroup):
    get_channel_url = State()
