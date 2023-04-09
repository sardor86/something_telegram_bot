from dataclasses import dataclass
from environs import Env
from gino import Gino

gino_db = Gino()


@dataclass
class DbConfig:
    host: str
    port: int
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


async def set_gino_db(data_base: DbConfig):
    await gino_db.set_bind(f'postgresql://{data_base.user}:'
                           f'{data_base.password}@'
                           f'{data_base.host}:{data_base.port}/'
                           f'{data_base.database}')


async def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    config = Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.str("ADMINS").split(","))),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            port=env.int('DB_PORT'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        )
    )

    await set_gino_db(config.db)

    return config
