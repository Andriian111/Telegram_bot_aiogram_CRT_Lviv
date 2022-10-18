import logging

from aiogram.types import CallbackQuery

from keyboards.inline.Captain_camp.upn.rouovyui_camp import zgoloshenya_rouovui
from keyboards.inline.members_camp.For_members import members_camp
from keyboards.inline.members_camp.covid_saved import covid_members
from keyboards.inline.members_camp.documents_for_camp import documents_members, approve_parents_kids, zgoloshenya_kids, \
    med_dovika_kids, copui_doc__kids
from keyboards.inline.members_camp.outfit_camp import out_fit_for_cammp
from loader import dp


@dp.callback_query_handler(text_contains="documentsforchild")#команда коли обираєш документи для учасників
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш необхідну інформацію про документи, які потрібно взяти на табір! \n"
                              "Зверни увагу, що організатори табору мають повне право не взяти тебе на табір, якщо ти забудеш щось! \n"
                              "Підготуйся заздалегідь!", reply_markup=documents_members)


@dp.callback_query_handler(text_contains="laststore")#команда повернутись до соновного списку по учасниках табору
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш необхідну інформацію про документи, які потрібно взяти на табір! \n"
                              "Зверни увагу, що організатори табору мають повне право не взяти тебе на табір, якщо ти забудеш щось! \n"
                              "Підготуйся заздалегідь!", reply_markup=members_camp)


@dp.callback_query_handler(text_contains="Covidsaveforchild")  # команда відкрити коронавірусну безпеку для учасників
async def covid_safe(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Тут ти знайдеш рекомендації по безпеці від коронавірусу під час проходження табору!"
                                  , reply_markup=covid_members)


@dp.callback_query_handler(text_contains="outfit")  # команда відкрити особистий виряд на табір
async def choose_outfit(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Тут ти знайдеш рекомендований особисти виряд на табір! \n "
                                  "Зверни увагу, що остатчоний список виряду ти отримаєш від проводу перед табору!"
                                  , reply_markup=out_fit_for_cammp)\


@dp.callback_query_handler(text_contains="documentsforchild")  # команда відкрити документи на табір
async def choose_outfit(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Тут ти знайдеш список документів, які обов'язково потрібно взяти на табір!"
                                  , reply_markup=documents_members)


@dp.callback_query_handler(text_contains="Acceptcampkids")  # команда відкрити по дозволу батьків
async def choise_book_campg(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Дозвіл від батьків на участь у таборі- мають заповнити твої батьки або опікуни. "
            "Перш ніж підписати дозвіл, необхідно добре ознайомитись з усіма правила табору. \n"
            , reply_markup=approve_parents_kids)

@dp.callback_query_handler(text_contains="zgoloshenyakids")  # команда зголошення на табір
async def choise_zgolosheny(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Зголошення учасника табору - потрібно заповнити перед початком табору і віддати організаторам табору."
                                  " Але, спочатку добре ознайомся з усіма вимогами та правилами проведення табору.",
                                  reply_markup=zgoloshenya_kids)


@dp.callback_query_handler(text_contains="medicaldockids")  # команда відкрити по медичній довідці курінний
async def choise_book_campg_kurinyu(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Медична довідка  є обов’язковим медичним документом для  участь у "
                                  "таборі. Без медичної довідки участь у таборі заборонена! "
                                  "\nМедична довідка зазвичай видається сімейним лікарем, не швидше ніж "
                                  "за 3 дні до початку табору. \n Подбай заздалегідь про це!",
                                  reply_markup=med_dovika_kids)


@dp.callback_query_handler(text_contains="copyofdocumentkids")  # команда копія документів
async def choise_copy_doc(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Кожен учасник табору повинен здати організаторам табору копію свідоцтва про народження "
            "або паспорта громадянина України до початку табору!",
            reply_markup=copui_doc__kids)


@dp.callback_query_handler(text_contains="comebackkidsdocuments")  # команда повернутись до книги
async def comeback_tobook(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Тут ти знайдеш необхідну інформацію про документи, які потрібно взяти на табір! "
            "Зверни увагу, що організатори табору мають повне право не взяти тебе на табір, якщо ти забудеш щось! "
            "Підготуйся заздалегідь!",
            reply_markup=documents_members)

