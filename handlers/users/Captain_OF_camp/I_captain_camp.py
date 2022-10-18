import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline.Captain_camp.Choise_ulad import lead_camp
from keyboards.inline.Captain_camp.upy.winter_camp import all_camp
from loader import dp


@dp.message_handler(Text(endswith=["Я комендант табору 🏕"])) #команда коли обираєш що ти комендант
async def choose(msg: Message):
    await msg.answer(text="Який плануєш робити табір?", reply_markup=all_camp)



@dp.callback_query_handler(text_contains="summercamp")  # команда відкрити літній табір
async def choise_summercamp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Від якого уладу плануєш робити табір ?",
                              reply_markup=lead_camp)

@dp.callback_query_handler(text_contains="timecamp")  # команда повернутись
async def comeback(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Який плануєш робити табір?", reply_markup=all_camp)


