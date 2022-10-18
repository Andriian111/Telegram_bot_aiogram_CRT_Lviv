
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from keyboards.inline.Trips.trips_all import trip_upy_child
from loader import dp


@dp.message_handler(Text(endswith=["Все про мандрівки ⛰"])) #команда відкрити все про мандрівки
async def choose(msg: Message):
    await msg.answer(text="Ось важлива інформація по організації мандрівки, яка тобі знадобиться!",reply_markup=trip_upy_child)

