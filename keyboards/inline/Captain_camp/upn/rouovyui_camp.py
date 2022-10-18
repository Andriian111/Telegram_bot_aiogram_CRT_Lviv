from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.Captain_camp.book_camp import magazine_tehn_safe, med_book_dorosla, med_book_buy, list_camper, \
    zgoloshenya, approve_from_contry, template_med, parents_aprove_template

rouovyi_camp = InlineKeyboardMarkup(row_width=1)
Claim_camp_r = InlineKeyboardButton(text="Вимоги для проведення ройових таборів",
                                  callback_data="choose:claimrouovui")#кнопка вимоги для проведення таборів
rouovyi_camp.insert(Claim_camp_r)
reporting_camp_r = InlineKeyboardButton(text="Зголошення ройових таборів",
                                      callback_data="choose:zgoloshenyarov")#кнопка зголосити гуртковий табір
rouovyi_camp.insert(reporting_camp_r)
book_camp_g = InlineKeyboardButton(text="Книга табору",
                                      callback_data="choose:bookcamprouoviy")#кнопка відкрити книгу гурткового табору
rouovyi_camp.insert(book_camp_g)
comeback_to_choise_upy_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktoupncamp")# кнопка повернутись на обрання курінного чи гурткового табору
rouovyi_camp.insert(comeback_to_choise_upy_camp)
# кнопки обрання по курінному таборі інформації



royovui_camp_come_back = InlineKeyboardMarkup(row_width=1)
comeback_to_choise_royov_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:backtocamproyovui")
royovui_camp_come_back.insert(comeback_to_choise_royov_camp)
# кнопка повернутись до ройового табору


vumohu_royovui = InlineKeyboardMarkup(row_width=1)
pered_camp_gnizdovui = InlineKeyboardButton(text=" Передтаборові вимоги",
                                           url="https://docs.google.com/document/d/1etSqb0U-e4Wj4z231Ze-_SncMPp"
                                               "teEsxuspKrQEN2I0/edit?usp=sharing")
vumohu_royovui.insert(pered_camp_gnizdovui)#кнопка передтаборові вимоги по табору
vumohu_camp_kurinui = InlineKeyboardButton( text = " Таборові вимоги",
                                            url="https://docs.google.com/document/")
vumohu_royovui.insert(vumohu_camp_kurinui)#кнопка вимоги по табору
vumohu_royovui.insert(comeback_to_choise_royov_camp)#кнопка повернутись на сторінку по курінному таборі
#вимоги до табору кнопки


Book_camp_rouoviu = InlineKeyboardMarkup(row_width=2)
Claim_dok = InlineKeyboardButton(text="Наказ на табір", callback_data="choose:claimdokrouovui")#кнопка наказу на табір
Book_camp_rouoviu.insert(Claim_dok)
list_camp = InlineKeyboardButton(text="Список учасників табору",
                                      callback_data="choose:listcamprouovui") #кнопка списку табору
Book_camp_rouoviu.insert(list_camp)

Accept_camp = InlineKeyboardButton(text="Дозволи батьків",
                                      callback_data="choose:Acceptrouovui") #кнопка дозволу батьків на табір
Book_camp_rouoviu.insert(Accept_camp)
insurance_camp = InlineKeyboardButton(text="Виписка про страхування ",
                                      callback_data="choose:insurancerouovui") #кнопка страхування
Book_camp_rouoviu.insert(insurance_camp)
medical_reference_camp = InlineKeyboardButton(text="Медична довідка",
                                      callback_data="choose:medicalreferencerouovui") #кнопка медичні довідки
Book_camp_rouoviu.insert(medical_reference_camp)
medical_book_camp = InlineKeyboardButton(text="Медична книжка",
                                      callback_data="choose:medicalbookrouovui") #кнопка медичні довідки
Book_camp_rouoviu.insert(medical_book_camp)
copy_of_document_camp = InlineKeyboardButton(text="Копії документів",
                                      callback_data="choose:copyofdocumentrouovui") #кнопка копії документів
Book_camp_rouoviu.insert(copy_of_document_camp)
rules_camp = InlineKeyboardButton(text="Правильник табору",
                                      callback_data="choose:rulesofrouovui") #кнопка правильника табору
Book_camp_rouoviu.insert(rules_camp)
journal_of_safety_briefing = InlineKeyboardButton(text="Журнал  техніки безпеки",
                                      callback_data="choose:journalofsafetyrouovui") #кнопка Журнал проведення інструктажу з техніки безпеки
Book_camp_rouoviu.insert(journal_of_safety_briefing)
sertuficat_PMD_gurt = InlineKeyboardButton(text="Сертифікат ДМД",
                                      callback_data="choose:sertuficatpmd") #кнопка сертифікату
Book_camp_rouoviu.insert(sertuficat_PMD_gurt)
Book_camp_rouoviu.insert(comeback_to_choise_royov_camp)#кнопка повернутись на сторінку по курінному таборі
#кнопки для книги табору


med_dovika_rouovui = InlineKeyboardMarkup(row_width=1)
med_dovika_rouovui.insert(approve_from_contry)#кнопка інструкції заповнення
med_dovika_rouovui.insert(template_med)#кнопка зразку мед довідки
comeback_to_choise_book_camp_rouovui = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktobookrouovui")
med_dovika_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#кнопки по мед довідці

approve_parents_rouovui = InlineKeyboardMarkup(row_width=1)
approve_parents_rouovui.insert(parents_aprove_template)#шаблон дозволу від батьків
approve_parents_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#кнопка дозволу від батьків

zgoloshenya_rouovui = InlineKeyboardMarkup(row_width=1)
zgoloshenya_rouovui.insert(zgoloshenya)#шаблон зголошення
zgoloshenya_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# #кнопка зголошення на табір

list_rouovui = InlineKeyboardMarkup(row_width=1)
list_rouovui.insert(list_camper)#зразок списку табору
list_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# #кнопка списку табору


insurance_rouovui = InlineKeyboardMarkup(row_width=1)
insurance_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка по страхуванню

med_book_rouovui = InlineKeyboardMarkup(row_width=1)
med_book_rouovui.insert(med_book_dorosla)#кнопка  на постанову
med_book_rouovui.insert(med_book_buy)#кнопка  на приклад
med_book_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка по медичну книжку


copui_doc__rouovui = InlineKeyboardMarkup(row_width=1)
copui_doc__rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка про копії документів

rules_rouovui = InlineKeyboardMarkup(row_width=1)
rules_rouovui.insert(rules_camp)
rules_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка про правильник табору

magazine_tehn_safe_rouovui= InlineKeyboardMarkup(row_width=1)
magazine_tehn_safe_rouovui.insert(magazine_tehn_safe)#кнопка приклад журнал провдення техніки безпеки
magazine_tehn_safe_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка про журнал техніки безпеки


sertuficat_DMD_rouovui = InlineKeyboardMarkup(row_width=1)
sertuficat_DMD = InlineKeyboardButton(text="Зголоситись на курси",
                                      callback_data="choose:trainDMD")
sertuficat_DMD_rouovui.insert(sertuficat_DMD)#кнопка зголоситись на вишкіл
sertuficat_DMD_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#сертифікат курсів ДМД


nakaz_rouovui = InlineKeyboardMarkup(row_width=1)
vymohu_pered_camp_rouovui =  InlineKeyboardButton(text="Передтаборові вимоги",
                                      url="https://docs.google.com/document/d/1etSqb0U-e4Wj4z231Ze-_SncMPpteEsxuspKrQEN"
                                          "2I0/edit?usp=sharing")#кнопка перед таборові вимоги
nakaz_rouovui.insert(vymohu_pered_camp_rouovui)
nakaz_rouovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#наказ на табір

