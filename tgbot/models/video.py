from .base import Base
from tgbot.config import gino_db


class Videos(Base):
    class VideosTable(gino_db.Model):
        __tablename__ = 'videos'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        video = gino_db.Column(gino_db.String())

    async def check_video_id(self, video_id: int) -> bool:
        return not await self.VideosTable.query.where(self.VideosTable.id == video_id).gino.first() is None

    async def add_video(self, video_token) -> int:
        video = self.VideosTable(video=video_token)

        await video.create()
        return video.id

    async def delete_video(self, video_id: int) -> bool:
        if await self.check_video_id(video_id):
            video = await self.VideosTable.query.where(self.VideosTable.id == video_id).gino.first()

            await video.delete()
            return True
        return False

    async def get_video(self):
        return await self.VideosTable.query.gino.first()


