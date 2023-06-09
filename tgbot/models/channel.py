from .base import Base
from tgbot.config import gino_db


class Channels(Base):
    class ChannelsTable(gino_db.Model):
        __tablename__ = 'channels'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        channel = gino_db.Column(gino_db.String(), unique=True)

    async def check_channel(self, channel: str) -> bool:
        return not await self.ChannelsTable.query.where(self.ChannelsTable.channel == channel).gino.first() is None

    async def check_channel_id(self, channel_id: int) -> bool:
        return not await self.ChannelsTable.query.where(self.ChannelsTable.id == channel_id).gino.first() is None

    async def add_channel(self, channel: str) -> int:
        if not await self.check_channel(channel):
            channel_in_db = self.ChannelsTable(channel=channel)

            await channel_in_db.create()
            return channel_in_db.id
        return -1

    async def delete_chanel(self, channel_id: int) -> bool:
        if await self.check_channel_id(channel_id):
            channel = await self.ChannelsTable.query.where(self.ChannelsTable.id == channel_id).gino.first()

            await channel.delete()
            return True
        return False

    async def get_all_channel(self) -> list:
        return await self.ChannelsTable.query.gino.all()
