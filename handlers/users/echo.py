from aiogram import types
from aiogram.types import Message

from loader import dp


@dp.message_handler(content_types=types.ContentTypes.TEXT) # відповісти на незрозуміле повідомлення
async def do_echo(msg: Message):
    text = msg.text
    if text and not text.startswith('/'):
        await msg.reply(text="Не зрозуміле повідомлення. Перед повідомленням постав ' / '  "
                             "\n Ось список доступних команд: \n"
                             "/start - розпочати/перезапустити додаток \n /aboutus - інформація про нас \n"
                             "/contacts - контакти \n"
                             "/openmenu - відновити кнопку меню в правому  нижньому куті \n"
                             "/help - отримати список команд")