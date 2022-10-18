import logging
from keyboards.inline.Captain_camp.ulad_upp import phatsch_camp, reporting_pschach_camp, Book_camp_upp, \
    traning_for_captain_camp_ptascach, vumohu_pschazch, list_ptaschui, copui_doc__ptaschui, \
    rules_ptaschui, magazine_tehn_safe_ptaschui, sertuficat_DMD_ptaschui, nakaz_ptaschui
from aiogram.types import CallbackQuery
from loader import dp


@dp.callback_query_handler(text_contains="upp")#команда коли обираєш улад упп
async def choise_UPP(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться", reply_markup=phatsch_camp)



@dp.callback_query_handler(text_contains="reportingptaschch")#зголосити пташачий табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Зголошення пташачих ",
                              reply_markup=reporting_pschach_camp)

@dp.callback_query_handler(text_contains="returntobookpschazch") #команда відкрити книгу табору
async def choise_come_back(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі табору ",
                              reply_markup=Book_camp_upp)


@dp.callback_query_handler(text_contains="comebacktopschazch")#повернутись на сторінку по інформації пташачий табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться.",
                              reply_markup=phatsch_camp)


@dp.callback_query_handler(text_contains="bookcampisptaschch") #команда відкрити книгу табору
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі табору ",
                              reply_markup=Book_camp_upp)


@dp.callback_query_handler(text_contains="vymohuptaschch")  # команда вимоги на табір
async def chise_vumohu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш вимоги до пташачих таборів",
                              reply_markup=vumohu_pschazch)

@dp.callback_query_handler(text_contains="trainptaschch")#відкрити зголошення на дошкіл  комендантів гніздових таборів
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Команда ЦРТ пропонуєте Тобі зголоситись на дошкіл для комендантів пташачих таборів, ",
                              reply_markup=traning_for_captain_camp_ptascach)\



@dp.callback_query_handler(text_contains="listcampptaschach")  # команда списку на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Список всіх учасників табору - заповнюється перед отриманням дозвілу (наказу) провдення табору. "
                              "Необхідно скинути заповенений список на електрону пошту станиці перед отриманням дозволу. "
                              "Повинен бути підписаний станичною або станичним та завірений мокрою печаткою.",
                              reply_markup=list_ptaschui)\


@dp.callback_query_handler(text_contains="copyofdocumentcampptaschach")  # команда копія документів
async def choise_copy_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен учасник табору повинен мати копію свідоцтва про народження або паспорта громадянина України \n",
                              reply_markup=copui_doc__ptaschui)\


@dp.callback_query_handler(text_contains="rulesofcampptaschach")  # команда відкрити правильник табору
async def choise_rules_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Правильник табору - набір правил на таборі, який зачитується на офіційному відкритті табору, "
                              "тим самим затверджується і входить дію, як правила перебування на таборі.\n",
                              reply_markup=rules_ptaschui)


@dp.callback_query_handler(text_contains="journalofsafetybriefingptaschach")  # команда журнал техніки безпеки
async def choise_magazine_safe(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Інструкаж техінки безпеки проводиться комендантом"
                              " на початку табору для усіх учасників, після цього "
                              "всі підписуються у журналі, що прослухали і ознайомились з технікою безпеки перебування на таборі. \n",
                              reply_markup=magazine_tehn_safe_ptaschui)\



@dp.callback_query_handler(text_contains="sertuficatpmdptaschach")  # команда сертифікати  ДМД
async def choise_sertuficat_DMD(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Сертифікат про відбутий тренінг видають на курсах домедичної допомоги.\n "
                              "Для отримання дозволу проведення табору комендант табору повинен подбати, щоб "
                              " у книзі табору було три діючих сертифікати з курсів домедичної допомоги.\n",
                              reply_markup=sertuficat_DMD_ptaschui)


@dp.callback_query_handler(text_contains="ptaschachclaimdok")  # команда наказу на табір
async def choise_claim_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Наказ на табір - це дозвіл станиці для проведення табору.\n Видається у разі виконання усіх "
                              "передтаборових вимог за 4-2 дні до початку табору у станиці.",
                              reply_markup=nakaz_ptaschui)


