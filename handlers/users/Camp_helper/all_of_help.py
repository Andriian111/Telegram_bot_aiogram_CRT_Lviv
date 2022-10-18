import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline.helper_camp.inventory import inventory_of_camp
from keyboards.inline.helper_camp.list_of_help import help_of_camp
from keyboards.inline.helper_camp.place_camp import place_of_camping
from loader import dp


@dp.message_handler(Text(endswith=["Таборовий помічник 🔰", "sdaf"])) #команда відкрити таборовий помічник
async def choose(msg: Message):
    await msg.answer(text="Тут ти знайдеш рекомендації, вимоги та ідеї для втілення табору!",reply_markup=help_of_camp)


@dp.callback_query_handler(text_contains="placeofcamp")#команда коли обираєш місце табору
async def choise_place_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш необхідну інформацію про вибір місця наметового табору", reply_markup=place_of_camping)


@dp.callback_query_handler(text_contains="reurnlistofhelp")#команда коли обираєш місце табору
async def reurn_list_of_help(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш рекомендації, вимоги та ідеї для втілення табору!",
                              reply_markup=help_of_camp)

@dp.callback_query_handler(text_contains="inventorycamp")#команда коли обираєш місце табору
async def inventory_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш рекоменданий та перевірений ремент для таборування!",
                              reply_markup=inventory_of_camp)