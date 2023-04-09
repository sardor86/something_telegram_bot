from aiogram import Dispatcher

from .admin import register_admin
from .add_video import register_add_video_handler


def register_admin_handlers(dp: Dispatcher):
    register_admin(dp)
    register_add_video_handler(dp)
