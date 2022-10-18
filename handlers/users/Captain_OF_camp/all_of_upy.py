import logging

from aiogram.types import CallbackQuery
from keyboards.inline.Captain_camp.Choise_ulad import lead_camp
from keyboards.inline.Captain_camp.Ulad_upy import UPY_camp
from keyboards.inline.Captain_camp.upy.gurtk_camp import gurtkov_camp, gurtkov_camp_come_back, train_gurtkovyu, \
    med_dovika_gurtk, Book_camp_gurt, approve_parents_gurtkoui, zgoloshenya_gurtkovui, insurance_gurtkovui, \
    med_book_gurtkovui, copui_doc__gurtkovui, rules_gurtkovui, magazine_tehn_safe_gurtkovui, list_gurtkovui, \
    nakaz_gurtkovui, sertuficat_DMD_gurtkovui, vumohu_gurtkovyu

from keyboards.inline.Captain_camp.upy.kyr_camp_upy import Kyr_camp, traning_for_captain_campkyr, Book_camp_f, \
    comeback_tp_kyr_camp, med_dovika_kurin, approve_parents_kurinui, zgoloshenya_kurinui, list_kurinui, \
    insurance_kurinui, med_book_kurinui, copui_doc__kurinui, rules_kurinui, magazine_tehn_safe_kurinui, \
    sertuficat_CRT_kurinui, sertuficat_DMD_kurinui, nakaz_kurinui, vumohu_kurinui
from loader import dp



@dp.callback_query_handler(text_contains="upy")#команда коли обираєш улад упю
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Вибери, який саме ти плануєш робити табір?", reply_markup=UPY_camp)


@dp.callback_query_handler(text_contains="kyrinuicamp") #команда коли обираєш курінний табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться", reply_markup=Kyr_camp)\


@dp.callback_query_handler(text_contains="claimcampkurinui") #команда коли обираєш курінний табір
async def choise_vumohu_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш вимоги до курінних таборів", reply_markup=vumohu_kurinui)


@dp.callback_query_handler(text_contains="comebacktoulad") #команда повернутись до обрання уладу
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Від якого уладу плануєш робити табір? ", reply_markup=lead_camp)


@dp.callback_query_handler(text_contains="comebacktoupycamp") #команда повернутись до обрання табору від упю
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться по курінному таборі",
                              reply_markup=UPY_camp)

@dp.callback_query_handler(text_contains="reportingcamp")#зголосити курінний табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Зголошення курінних таборів буде відкрите у травні 2021 року.",
                              reply_markup=comeback_tp_kyr_camp)


@dp.callback_query_handler(text_contains="comebacktokyrcamp")#повернутись на сторінку по інформації на курінний табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться.",
                              reply_markup=Kyr_camp)


@dp.callback_query_handler(text_contains="traink")#відкрити зголошення на вишкіл комендантів
async def choise_traink(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Команда ЦРТ пропонуєте Тобі зголоситись на вишкіл для комендантів курінних таборів, "
                              "який буде відбуватись 20-21 березня. Кількість місць на  вишкіл обмежена.\n",
                              reply_markup=traning_for_captain_campkyr)


@dp.callback_query_handler(text_contains="bookcampkyr") #команда відкрити книгу табору
async def choise_bookCamp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі табору ",
                              reply_markup=Book_camp_f)

@dp.callback_query_handler(text_contains="comebacktobookkurinyui")  # команда повернутись до книги курінного табору
async def comeback_book_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі курінного табору ",
                              reply_markup=Book_camp_f)


@dp.callback_query_handler(text_contains="medicalreferencecamp")  # команда відкрити по медичній довідці курінний
async def choise_book_campg_kurinyu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Медична довідка  є обов’язковим медичним документом для дітей, які беруть участь у "
                              "наметовому таборі. Без медичної довідки участь у таборі заборонена! "
                              "\nМедична довідка зазвичай видається сімейним лікарем, не швидше ніж "
                              "за 3 дні до початку табору.",
                              reply_markup=med_dovika_kurin)


@dp.callback_query_handler(text_contains="Acceptcampkurinui")  # команда відкрити по дозволу батьків
async def choise_book_campg_kurinyu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Дозвіл від батьків - заповнюють батьки або опікуни дитина, яка планує брати участь у таборі."
                              "\nПідписуючи дозвіл батьки або опікуни погоджються з усіма правилами табору "
                              "та надають дозвіл дитині брати участь у таборі.\n",

                              reply_markup=approve_parents_kurinui)

@dp.callback_query_handler(text_contains="zgoloshenyamembercamp")  # команда зголошення на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Зголошення учасника табору - заповнюють перед початком табору, "
                              "тим самим погоджуються з усіма вимогами та правилами проведення табору.\n",
                              reply_markup=zgoloshenya_kurinui)


@dp.callback_query_handler(text_contains="listkurinuicap")  # команда списку на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Список всіх учасників табору - заповнюється перед отриманням дозвілу (наказу) провдення табору. "
                              "Необхідно скинути заповенений список на електрону пошту станиці перед отриманням дозволу. "
                              "Повинен бути підписаний станичною або станичним та завірений мокрою печаткою.",
                              reply_markup=list_kurinui)\


@dp.callback_query_handler(text_contains="insurancekurinui")  # команда страхування на табір
async def choise_insurence(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен учасник табору повинен бути застрохавним в будь-які страховій компанії. Станиця Львів "
                              "централізовано кожного року страхує всі дітей у страховій компанії PZU від нещасних випадків. \n"
                              "Виписку про страхування учасників табору можна отримати при отриманні дозволу (наказу) на табір"
                              " в станиці. \n"
                              " У разі відсутності когось із учасників табору у виписці про страхування -"
                              " необхідно мати страховий поліс!",
                              reply_markup=insurance_kurinui)\


@dp.callback_query_handler(text_contains="medicalbookkurnui")  # команда медичну книжку на табір
async def choise_med_book(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен член команди організаторів перед табором повинен пройти медичний огляд "
                              "та під час проходження табору мати при собі заповнену"
                              " медичну особову книжку. Можна придбати у будь-яких канцелярських магазинах."
                              " \n Участь у таборі без медичної книжки заборонена! \n",
                              reply_markup=med_book_kurinui)\


@dp.callback_query_handler(text_contains="copyofdocumentkurinui")  # команда медичну книжку на табір
async def choise_copy_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен учасник табору повинен мати копію свідоцтва про народження або паспорта громадянина України \n",
                              reply_markup=copui_doc__kurinui)\


@dp.callback_query_handler(text_contains="rulesofkurinui")  # команда відкрити правильник табору
async def choise_rules_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Правильник табору - набір правил на таборі, який зачитується на офіційному відкритті табору, "
                              "тим самим затверджується і входить дію, як правила перебування на таборі.\n",
                              reply_markup=rules_kurinui)


@dp.callback_query_handler(text_contains="journalofsafetykurinui")  # команда відкрити правильник табору
async def choise_magazine_safe(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Інструкаж техінки безпеки проводиться комендантом"
                              " на початку табору для усіх учасників, після цього "
                              "всі підписуються у журналі, що прослухали і ознайомились з технікою безпеки перебування на таборі. \n",
                              reply_markup=magazine_tehn_safe_kurinui)\


@dp.callback_query_handler(text_contains="sertuficatcrt")  # команда відкрити правильник табору
async def choise_sertuficat_CRT(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Сертифікат проходження вишколу від ЦРТ видається усім учасникам вишколу, які відбули вишкіл. "
                              "Для отримання дозволу проведення табору комендант табору повинен подбати, щоб сертифікат"
                              " був у книзі табору. Можна використати сертифікат проходження вишколу ЦРТ у 2019 році.\n",
                              reply_markup=sertuficat_CRT_kurinui)\


@dp.callback_query_handler(text_contains="sertuficatpmdkurinyui")  # команда сертифікати  ДМД
async def choise_sertuficat_DMD(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Сертифікат про відбутий тренінг видають на курсах домедичної допомоги.\n "
                              "Для отримання дозволу проведення табору комендант табору повинен подбати, щоб "
                              " у книзі табору було три діючих сертифікати з курсів домедичної допомоги.\n",
                              reply_markup=sertuficat_DMD_kurinui)


@dp.callback_query_handler(text_contains="claimdokkurinui")  # команда сертифікати  ДМД
async def choise_claim_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Наказ на табір - це дозвіл станиці для проведення табору.\n Видається у разі виконання усіх "
                              "передтаборових вимог за 4-2 дні до початку табору у станиці.",
                              reply_markup=nakaz_kurinui)



#ГУРТКОВИЙ ТАБІР НИЖЧЕ
@dp.callback_query_handler(text_contains="gcamp")  # команда відкрити книгу табору
async def choise_bookCamp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Ось важлива інформація по табору, яка тобі знадобиться ",
                              reply_markup=gurtkov_camp)


@dp.callback_query_handler(text_contains="Claimcampgurtkovui") #команда коли вимоги
async def choise_vumohu_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш вимоги до гурткових таборів", reply_markup=vumohu_gurtkovyu)


@dp.callback_query_handler(text_contains="zgoloshenyagurt")  # команда відкрити зголошення таборів
async def choise_reporting_camp_gurt(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Зголошення гурткових таборів буде відкрито у травні 2020 року",
                              reply_markup=gurtkov_camp_come_back)

@dp.callback_query_handler(text_contains="backtogurtkovyh")  # команда повернутись до гурткового табору
async def choise_back_to_camp_gurtkovyu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Ось важлива інформація по табору, яка тобі знадобиться",
                              reply_markup=gurtkov_camp)\


@dp.callback_query_handler(text_contains="traingurt")  # команда повернутись до гурткового табору
async def choise_train_gurt_captain(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Команда ЦРТ організовує вишкіл для комендантів гуртоквих таборів, який буде відбуватись "
                              "27-28 березня.",
                              reply_markup=train_gurtkovyu)\


@dp.callback_query_handler(text_contains="bookcampgurtk")  # команда відкрити книгу  гурткового табору
async def choise_book_campg_urtk(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі гурткового табору ",
                              reply_markup=Book_camp_gurt)\


@dp.callback_query_handler(text_contains="meddocumentgurtkovoi")  # команда відкрити по медичній довідці гуртковий
async def choise_book_campg_urtk(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Медична довідка  є обов’язковим медичним документом для дітей, які беруть участь у "
                              "наметовому таборі. Без медичної довідки участь у таборі заборонена! "
                              "\nМедична довідка зазвичай видається сімейним лікарем, не швидше ніж "
                              "за 3 дні до початку табору.",
                              reply_markup=med_dovika_gurtk)


@dp.callback_query_handler(text_contains="returntobookgurtkovui")  # команда повернутись до книги гурткового табору
async def comeback_book_gurtkovui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі гурткового табору ",
                              reply_markup=Book_camp_gurt)

@dp.callback_query_handler(text_contains="Acceptgurtkovui")  # команда відкрити по дозволу батьків
async def choise_book_campg_gurtkovui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Дозвіл від батьків - заповнюють батьки або опікуни дитина, яка планує брати участь у таборі."
                              "\nПідписуючи дозвіл батьки або опікуни погоджються з усіма правилами табору "
                              "та надають дозвіл дитині брати участь у таборі.\n",

                              reply_markup=approve_parents_gurtkoui)

@dp.callback_query_handler(text_contains="zgoloshenygurtkovui")  # команда зголошення на табір
async def choise_zgolosheny_gurtkov(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Зголошення учасника табору - заповнюють перед початком табору, "
                              "тим самим погоджуються з усіма вимогами та правилами проведення табору.\n",
                              reply_markup=zgoloshenya_gurtkovui)


@dp.callback_query_handler(text_contains="insurancegurtkovui")  # команда страхування на табір
async def choise_insurence(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен учасник табору повинен бути застрохавним в будь-які страховій компанії. Станиця Львів "
                              "централізовано кожного року страхує всі дітей у страховій компанії PZU від нещасних випадків. \n"
                              "Виписку про страхування учасників табору можна отримати при отриманні дозволу (наказу) на табір"
                              " в станиці. \n"
                              " У разі відсутності когось із учасників табору у виписці про страхування -"
                              " необхідно мати страховий поліс!",
                              reply_markup=insurance_gurtkovui)



@dp.callback_query_handler(text_contains="medicalbookgurtkovui")  # команда медичну книжку на табір
async def choise_med_book(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Кожен член команди організаторів перед табором повинен пройти медичний огляд "
                                  "та під час проходження табору мати при собі заповнену"
                                  " медичну особову книжку. Можна придбати у будь-яких канцелярських магазинах."
                                  " \n Участь у таборі без медичної книжки заборонена! \n",
                                  reply_markup=med_book_gurtkovui)

@dp.callback_query_handler(text_contains="copyofdocumentgurtkovui")  # команда медичну книжку на табір
async def choise_copy_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен учасник табору повинен мати копію свідоцтва про народження або паспорта громадянина України \n",
                              reply_markup=copui_doc__gurtkovui)


@dp.callback_query_handler(text_contains="rulesofgurtkovui")  # команда відкрити правильник табору
async def choise_rules_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Правильник табору - набір правил на таборі, який зачитується на офіційному відкритті табору, "
                              "тим самим затверджується і входить у дію, як правила перебування на таборі.\n",
                              reply_markup=rules_gurtkovui)\


@dp.callback_query_handler(text_contains="journalofsafetgurtkovui")  # команда відкрити правильник табору
async def choise_magazine_safe(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Інструкаж техінки безпеки проводиться комендантом"
                              " на початку табору для усіх учасників, після цього "
                              "всі підписуються у журналі, що прослухали і ознайомились з технікою безпеки перебування на таборі. \n",
                              reply_markup=magazine_tehn_safe_gurtkovui)


@dp.callback_query_handler(text_contains="listgurtkovui")  # команда списку на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Список всіх учасників табору - заповнюється перед отриманням дозвілу (наказу) провдення табору. "
                              "Необхідно скинути заповенений список на електрону пошту станиці перед отриманням дозволу. "
                              "Повинен бути підписаний станичною або станичним та завірений мокрою печаткою.",
                              reply_markup=list_gurtkovui)

@dp.callback_query_handler(text_contains="claimdokgurtkovui")  # команда сертифікати  ДМД
async def choise_claim_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Наказ на табір - це дозвіл станиці для проведення табору.\n Видається у разі виконання усіх "
                              "передтаборових вимог за 4-2 дні до початку табору у станиці.",
                              reply_markup=nakaz_gurtkovui)


@dp.callback_query_handler(text_contains="sertuficatpmdgurtkovui")  # команда сертифікати  ДМД
async def choise_sertuficat_DMD(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Сертифікат про відбутий тренінг видають на курсах домедичної допомоги.\n "
                              "Для отримання дозволу проведення табору комендант табору повинен подбати, щоб "
                              " у книзі гуртковго табору був один діючий сертифікат з курсу домедичної допомоги.\n",
                              reply_markup=sertuficat_DMD_gurtkovui)