from aiogram.types import Message
from bot import dp, bot
from bot.api import TikTokAPI


TikTok = TikTokAPI(
    link='tiktok.com',
    regexp_key=r'"video":{"id":"(.*?)",.*?"downloadAddr":"(.*?)",.*?}',
    headers={
        "Referer": "https://www.tiktok.com/",
    }
)


@dp.message_handler()
async def get_message(message: Message):
    async for video in TikTok.handle_message(message):
        if not video: continue
        await bot.send_video(message.chat.id, video, reply_to_message_id=message.message_id)
