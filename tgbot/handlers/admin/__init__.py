from aiogram import Dispatcher

from .admin import register_admin
from .add_video import register_add_video_handler
from .delete_video import register_delete_video_handler
from .add_chanel import register_add_chanel_handlers
from .delete_channel import register_delete_channel_handler


def register_admin_handlers(dp: Dispatcher):
    register_admin(dp)
    register_add_video_handler(dp)
    register_delete_video_handler(dp)
    register_add_chanel_handlers(dp)
    register_delete_channel_handler(dp)
