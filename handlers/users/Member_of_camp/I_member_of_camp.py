from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.inline.members_camp.For_members import members_camp
from loader import dp


@dp.message_handler(Text(endswith=["Я учасник табору ⛺️"]))#команда коли обираєш улад упю
async def choise_UPY(msg: Message):
    await msg.answer("Тут ти знайдеш корисну інформацію по табору", reply_markup=members_camp)