from aiogram.dispatcher.filters.state import StatesGroup, State


class AddVideo(StatesGroup):
    get_video = State()

