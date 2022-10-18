import logging

from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.types import Message
from keyboards.inline.course_DMD.April import April_course
from keyboards.inline.course_DMD.Februar import Februar_course
from keyboards.inline.course_DMD.Info_course import Info_to_course
from keyboards.inline.course_DMD.March import march_course

from loader import dp


@dp.message_handler(Text(endswith=["Курси домедичної допомоги ⛑"]))#команда відкрити курси ДМД
async def choise_course(msg: Message):
    await msg.answer("Центр Розвитку Табріництва проводить разом з Мальтійською службою допомоги курси домедичної"
                     " допомоги.\n"
                     "Детальна інформація по курсах: \n"
                     "Тривалість курсу - 8 годин  (може бути розбитий на два дні по 4 години)\n"
                     "Вартість курсу - 200 грн з особи. \n"
                     "Вимоги для участі у курсах: \n"
                     "Вік - 16+ років\n"
                     "📆"
                     "", reply_markup=Info_to_course)

@dp.callback_query_handler(text_contains="trainDMD")  # команда лютий
async def choose_Februar(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Центр Розвитку Табріництва проводить разом з Мальтійською службою допомоги курси домедичної"
                     " допомоги.  \n"
                     "Детальна інформація по курсах: \n"
                     "Тривалість курсу - 8 годин  (може бути розбитий на два дні по 4 години)\n"
                     "Вартість курсу - 200 грн з особи. \n"
                     "Вимоги для участі у курсах: \n"
                     "Вік - 16+ років\n"
                                  "📆"
                     "", reply_markup=Info_to_course)

@dp.callback_query_handler(text_contains="March")  # команда березень
async def choose_March(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Вибири зручні дати для проходження курсу 👇 "
                                  , reply_markup=march_course)


@dp.callback_query_handler(text_contains="Februar")  # команда лютий
async def choose_Februar(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Вибири зручні дати для проходження курсу 👇"
                                  , reply_markup=Februar_course)


@dp.callback_query_handler(text_contains="April")  # команда квітень
async def choose_April(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Дати для проходження курсів у квітні, поки що не доступні",
                                  reply_markup=April_course)


@dp.callback_query_handler(text_contains="comebacktochoisemonth")  # команда квітень
async def choose_comeback(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Центр Розвитку Табріництва проводить разом з Мальтійською службою допомоги курси домедичної"
                     " допомоги. Вміти надати домедичну допомогу до приїзду лікаря - повинен кожен член команди "
                     "організаторів табору! \n"
                     "Детальна інформація по курсах: \n"
                     "Тривалість курсу - 8 годин  (може бути розбитий на два дні по 4 години)\n"
                     "Вартість курсу - 150 грн з особи. \n"
                     "Вимоги для участі у курсах: \n"
                     "Вік - 16+ років\n"
                     "Для проведення табору в команді організаторів повинно бути мінімум три особи,"
                     " які пройшли курси та мають діючий сертифікат!"
                     "", reply_markup=Info_to_course)


