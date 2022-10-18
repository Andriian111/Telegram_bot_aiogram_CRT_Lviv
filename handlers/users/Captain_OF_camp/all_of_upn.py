import logging
from aiogram.types import CallbackQuery
from keyboards.inline.Captain_camp.Ulad_Upn import Upn_camp
from keyboards.inline.Captain_camp.upn.gnizdovyu_camp import traning_for_captain_campgnizd, Book_camp_upn, gniz_camp, \
    nakaz_gnizdovui, sertuficat_DMD_gnizdovui, med_dovika_gnizdovui, approve_parents_gnizdovui, \
    zgoloshenya_gnizdovui, list_gnizdovui, insurance_gnizdovui, med_book_gnizdovui, copui_doc__gnizdovui, \
    rules_gnizdovui, magazine_tehn_safe_gnizdovui, vumohu_gnizdovui, comeback_tp_gnizd_camp
from keyboards.inline.Captain_camp.upn.rouovyui_camp import rouovyi_camp, royovui_camp_come_back, Book_camp_rouoviu, \
    vumohu_royovui, nakaz_rouovui, sertuficat_DMD_rouovui, magazine_tehn_safe_rouovui, rules_rouovui, \
    copui_doc__rouovui, med_book_rouovui, insurance_rouovui, list_rouovui, zgoloshenya_rouovui, approve_parents_rouovui, \
    med_dovika_rouovui
from keyboards.inline.Captain_camp.upy.kyr_camp_upy import nakaz_kurinui, sertuficat_DMD_kurinui, zgoloshenya_kurinui, \
    approve_parents_kurinui
from loader import dp


@dp.callback_query_handler(text_contains="upn") #команда відкрити улад упн
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Вкажи, який саме ти плануєш робити табір?  ",
                              reply_markup=Upn_camp)


@dp.callback_query_handler(text_contains="gnizcamp") #команда відкрити гніздовий табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут знайдеш важливу іноформацію по гніздових таборах  ",
                              reply_markup=gniz_camp)


@dp.callback_query_handler(text_contains="reportinggnizdcamp")#зголосити гніздовий табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Зголошення гніздових таборів буде відкрите у травні 2021 року.",
                              reply_markup=comeback_tp_gnizd_camp)


@dp.callback_query_handler(text_contains="comebacktognizdcamp")#повернутись на сторінку по інформації на гніздовому табір
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться.",
                              reply_markup=gniz_camp)


@dp.callback_query_handler(text_contains="bookcampisgnizd") #команда відкрити книгу табору
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі табору ",
                              reply_markup=Book_camp_upn)



@dp.callback_query_handler(text_contains="traingnizd")#відкрити зголошення на дошкіл  комендантів гніздових таборів
async def choise_UPY(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Команда ЦРТ пропонуєте Тобі зголоситись на вишкіл для комендантів курінних таборів, "
                              "який буде відбуватись у два заходи. Обери для тезручну дату!. "
                              "Увага! ЦРТ буде дозволяти проводити крінні табори лише тим, хто має сертифікат з "
                              "проходження вишколу від ЦРТ(Може мати хтось з команди)",
                              reply_markup=traning_for_captain_campgnizd)\



@dp.callback_query_handler(text_contains="zgoloshenyarov")#вибрати зголошення табору
async def choise_zgoloshenya_camp_rov(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Зголошення ройових таборів буде відкрито у травні 2021 року",
                              reply_markup=royovui_camp_come_back)\


@dp.callback_query_handler(text_contains="backtocamproyovui")#повернутись до ройового табору
async def choise_back_to_camp_royovui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться",
                              reply_markup=rouovyi_camp)\

@dp.callback_query_handler(text_contains="bookcamprouoviy")#відкрити книгу гурткового табору
async def choise_book_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Тут ти знайдеш список документів, які мають бути в книзі ройового табору ",
                              reply_markup=Book_camp_rouoviu)

@dp.callback_query_handler(text_contains="comebacktobookgnizdovui")  # команда повернутись до книги гніздового табору
async def comeback_book_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш список документів, які мають бути в книзі гніздового табору ",
                              reply_markup=Book_camp_upn)\

@dp.callback_query_handler(text_contains="comebacktognizdgnizdovui")  # команда повернутись  гніздового табору
async def comeback_gnizdovui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут знайдеш важливу іноформацію по гніздових таборах",
                              reply_markup=gniz_camp)\


@dp.callback_query_handler(text_contains="vumohugnizdovui")  # команда вимоги на табір
async def chise_vumohu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer(" Тут ти знайдеш вимоги до гніздових таборів",
                              reply_markup=vumohu_gnizdovui)


@dp.callback_query_handler(text_contains="medicalreferencegnizdovui")  # команда відкрити по медичній довідці курінний
async def choise_book_campg_kurinyu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Медична довідка  є обов’язковим медичним документом для дітей, які беруть участь у "
                              "наметовому таборі. Без медичної довідки участь у таборі заборонена! "
                              "\nМедична довідка зазвичай видається сімейним лікарем, не швидше ніж "
                              "за 3 дні до початку табору.",
                              reply_markup=med_dovika_gnizdovui)


@dp.callback_query_handler(text_contains="Acceptgnizdovui")  # команда відкрити по дозволу батьків
async def choise_book_campg_kurinyu(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Дозвіл від батьків - заповнюють батьки або опікуни дитина, яка планує брати участь у таборі."
                              "\nПідписуючи дозвіл батьки або опікуни погоджються з усіма правилами табору "
                              "та надають дозвіл дитині брати участь у таборі.\n",

                              reply_markup=approve_parents_gnizdovui)

@dp.callback_query_handler(text_contains="zgoloshenyagnizdovui")  # команда зголошення на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Зголошення учасника табору - заповнюють перед початком табору, "
                              "тим самим погоджуються з усіма вимогами та правилами проведення табору.\n",
                              reply_markup=zgoloshenya_gnizdovui)


@dp.callback_query_handler(text_contains="listcampgnizdovui")  # команда списку на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Список всіх учасників табору - заповнюється перед отриманням дозвілу (наказу) провдення табору. "
                              "Необхідно скинути заповенений список на електрону пошту станиці перед отриманням дозволу. "
                              "Повинен бути підписаний станичною або станичним та завірений мокрою печаткою.",
                              reply_markup=list_gnizdovui)\


@dp.callback_query_handler(text_contains="insurancegnizdovui")  # команда страхування на табір
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
                              reply_markup=insurance_gnizdovui)\


@dp.callback_query_handler(text_contains="medicalbookcampgnizdovui")  # команда медичну книжку на табір
async def choise_med_book(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен член команди організаторів перед табором повинен пройти медичний огляд "
                              "та під час проходження табору мати при собі заповнену"
                              " медичну особову книжку. Можна придбати у будь-яких канцелярських магазинах."
                              " \n Участь у таборі без медичної книжки заборонена! \n",
                              reply_markup=med_book_gnizdovui)\


@dp.callback_query_handler(text_contains="copyofdocumentgnizdovui")  # команда копія документів
async def choise_copy_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Кожен учасник табору повинен мати копію свідоцтва про народження або паспорта громадянина України \n",
                              reply_markup=copui_doc__gnizdovui)\


@dp.callback_query_handler(text_contains="rulesofgnizdovui")  # команда відкрити правильник табору
async def choise_rules_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Правильник табору - набір правил на таборі, який зачитується на офіційному відкритті табору, "
                              "тим самим затверджується і входить дію, як правила перебування на таборі.\n",
                              reply_markup=rules_gnizdovui)


@dp.callback_query_handler(text_contains="journalofsafegnizdovui")  # команда журнал техніки безпеки
async def choise_magazine_safe(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Інструкаж техінки безпеки проводиться комендантом"
                              " на початку табору для усіх учасників, після цього "
                              "всі підписуються у журналі, що прослухали і ознайомились з технікою безпеки перебування на таборі. \n",
                              reply_markup=magazine_tehn_safe_gnizdovui)\



@dp.callback_query_handler(text_contains="sertuficatpmdgnizdovui")  # команда сертифікати  ДМД
async def choise_sertuficat_DMD(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Сертифікат про відбутий тренінг видають на курсах домедичної допомоги.\n "
                              "Для отримання дозволу проведення табору комендант табору повинен подбати, щоб "
                              " у книзі табору було три діючих сертифікати з курсів домедичної допомоги.\n",
                              reply_markup=sertuficat_DMD_gnizdovui)


@dp.callback_query_handler(text_contains="claimdokgnizdovui")  # команда наказу на табір
async def choise_claim_doc(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Наказ на табір - це дозвіл станиці для проведення табору.\n Видається у разі виконання усіх "
                              "передтаборових вимог за 4-2 дні до початку табору у станиці.",
                              reply_markup=nakaz_gnizdovui)


#РОЙОВИЙ ТАБІР
@dp.callback_query_handler(text_contains="rovcamp")  # відкрити ройовий табір
async def choise_royovui_camp(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call={callback_data}")
    await call.message.answer("Ось важлива інформація по табору, яка тобі знадобиться",
                              reply_markup=rouovyi_camp)


@dp.callback_query_handler(text_contains="claimrouovui")# команда вимоги на табір
async def chise_vumohu(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(" Тут ти знайдеш вимоги до гніздових таборів",
                                  reply_markup=vumohu_royovui)


@dp.callback_query_handler(text_contains="medicalreferencerouovui")  # команда відкрити по медичній довідці курінний
async def choise_book_campg_kurinyu(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Медична довідка  є обов’язковим медичним документом для дітей, які беруть участь у "
                                  "наметовому таборі. Без медичної довідки участь у таборі заборонена! "
                                  "\nМедична довідка зазвичай видається сімейним лікарем, не швидше ніж "
                                  "за 3 дні до початку табору.",
                                  reply_markup=med_dovika_rouovui)

@dp.callback_query_handler(text_contains="Acceptrouovui")  # команда відкрити по дозволу батьків
async def choise_book_campg_kurinyu(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Дозвіл від батьків - заповнюють батьки або опікуни дитина, яка планує брати участь у таборі."
            "\nПідписуючи дозвіл батьки або опікуни погоджються з усіма правилами табору "
            "та надають дозвіл дитині брати участь у таборі.\n",

            reply_markup=approve_parents_rouovui)

@dp.callback_query_handler(text_contains="zgoloshenyamemberrouovui")  # команда зголошення на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Зголошення учасника табору - заповнюють перед початком табору, "
                                  "тим самим погоджуються з усіма вимогами та правилами проведення табору.\n",
                                  reply_markup=zgoloshenya_rouovui)

@dp.callback_query_handler(text_contains="listcamprouovui")  # команда списку на табір
async def choise_zgolosheny_kurinui(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Список всіх учасників табору - заповнюється перед отриманням дозвілу (наказу) провдення табору. "
            "Необхідно скинути заповенений список на електрону пошту станиці перед отриманням дозволу. "
            "Повинен бути підписаний станичною або станичним та завірений мокрою печаткою.",
            reply_markup=list_rouovui) \

@dp.callback_query_handler(text_contains="insurancerouovui")  # команда страхування на табір
async def choise_insurence(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Кожен учасник табору повинен бути застрохавним в будь-які страховій компанії. Станиця Львів "
            "централізовано кожного року страхує всі дітей у страховій компанії PZU від нещасних випадків. \n"
            "Виписку про страхування учасників табору можна отримати при отриманні дозволу (наказу) на табір"
            " в станиці. \n"
            " У разі відсутності когось із учасників табору у виписці про страхування -"
            " необхідно мати страховий поліс!",
            reply_markup=insurance_rouovui) \


@dp.callback_query_handler(text_contains="medicalbookrouovui")  # команда медичну книжку на табір
async def choise_med_book(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Кожен член команди організаторів перед табором повинен пройти медичний огляд "
                                  "та під час проходження табору мати при собі заповнену"
                                  " медичну особову книжку. Можна придбати у будь-яких канцелярських магазинах."
                                  " \n Участь у таборі без медичної книжки заборонена! \n",
                                  reply_markup=med_book_rouovui) \


@dp.callback_query_handler(text_contains="copyofdocumentrouovui")  # команда копія документів
async def choise_copy_doc(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Кожен учасник табору повинен мати копію свідоцтва про народження або паспорта громадянина України \n",
            reply_markup=copui_doc__rouovui) \


@dp.callback_query_handler(text_contains="rulesofrouovui")  # команда відкрити правильник табору
async def choise_rules_camp(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Правильник табору - набір правил на таборі, який зачитується на офіційному відкритті табору, "
            "тим самим затверджується і входить дію, як правила перебування на таборі.\n",
            reply_markup=rules_rouovui)

@dp.callback_query_handler(text_contains="journalofsafetyrouovui")  # команда журнал техніки безпеки
async def choise_magazine_safe(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Інструкаж техінки безпеки проводиться комендантом"
                                  " на початку табору для усіх учасників, після цього "
                                  "всі підписуються у журналі, що прослухали і ознайомились з технікою безпеки перебування на таборі. \n",
                                  reply_markup=magazine_tehn_safe_rouovui)



@dp.callback_query_handler(text_contains="sertuficatpmd")  # команда сертифікати  ДМД
async def choise_sertuficat_DMD(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer("Сертифікат про відбутий тренінг видають на курсах домедичної допомоги.\n "
                                  "Для отримання дозволу проведення табору комендант табору повинен подбати, щоб "
                                  " у книзі табору був один діючий сертифікат з курсу домедичної допомоги.\n",
                                  reply_markup=sertuficat_DMD_rouovui)

@dp.callback_query_handler(text_contains="claimdokrouovui")  # команда наказу на табір
async def choise_claim_doc(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Наказ на табір - це дозвіл станиці для проведення табору.\n Видається у разі виконання усіх "
            "передтаборових вимог за 4-2 дні до початку табору у станиці.",
            reply_markup=nakaz_rouovui)\



@dp.callback_query_handler(text_contains="comebacktobookrouovui")  # команда повернутись до книги
async def comeback_tobook(call: CallbackQuery):
        await call.answer(cache_time=60)
        callback_data = call.data
        logging.info(f"call={callback_data}")
        await call.message.answer(
            "Тут ти знайдеш список документів, які мають бути в книзі ройового табору.",
            reply_markup=Book_camp_rouoviu)




