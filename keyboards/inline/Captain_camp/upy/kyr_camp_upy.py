from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.Captain_camp.book_camp import approve_from_contry, template_med, parents_aprove_template, \
    zgoloshenya, list_camper, med_book_dorosla, med_book_buy, magazine_tehn_safe

Kyr_camp = InlineKeyboardMarkup(row_width=1)
Claim_camp = InlineKeyboardButton(text="Вимоги для проведення таборів 💬📌",
                                  callback_data="choose:claimcampkurinui") #кнопка вимоги для проведення таборів
Kyr_camp.insert(Claim_camp)
reporting_camp = InlineKeyboardButton(text="Зголошення курінних таборів  🆘📢",
                                      callback_data="choose:reportingcamp")#кнопка зголосити курінний табір
Kyr_camp.insert(reporting_camp)
train_k = InlineKeyboardButton(text="Вишкіл комендантів курінних таборів ⏳📚",
                                      callback_data="choose:traink")#кнопка про вишкіл коменданта
Kyr_camp.insert(train_k)
book_camp = InlineKeyboardButton(text="Книга табору 📒❗️",
                                      callback_data="choose:bookcampkyr")#кнопка відкрити книгу табору
Kyr_camp.insert(book_camp)
comeback_to_choise_upy_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktoupycamp")# кнопка повернутись на обрання курінного чи гурткового табору
Kyr_camp.insert(comeback_to_choise_upy_camp)
# кнопки обрання по курінному таборі інформації


comeback_tp_kyr_camp = InlineKeyboardMarkup(row_width=1)
comeback_to_choise_upy_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktokyrcamp")
comeback_tp_kyr_camp.insert(comeback_to_choise_upy_camp)
# кнопка повернення на обрання по  курінному таборі інформації


traning_for_captain_campkyr = InlineKeyboardMarkup(row_width=1)
traning_for_captain_campkyrbutton_March_15_16= InlineKeyboardButton(text="20-21 березня ",
                                      url="https://docs.google.com/forms/d/1X1jp3OyPEnK8mpcgue"
                                          "Jc5G9PfVVI0chqQ7mIx0911_Y/edit")
traning_for_captain_campkyr.insert(traning_for_captain_campkyrbutton_March_15_16)# кнопка зголошення на вишкіл комендантів на 15-16 березня
comeback_to_choise_kcamp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktokyrcamp")
traning_for_captain_campkyr.insert(comeback_to_choise_kcamp) #кнопка повернутись на сторінку по курінному таборі
# кнопки зголошення на вишкіл комендантів


vumohu_kurinui = InlineKeyboardMarkup(row_width=1)
pered_camp_kurinui = InlineKeyboardButton(text=" Передтаборові вимоги",
                                           url="https://docs.google.com/document/d/1etSqb0U-e4Wj4z231Ze-_SncMPp"
                                               "teEsxuspKrQEN2I0/edit?usp=sharing")
vumohu_kurinui.insert(pered_camp_kurinui)#кнопка передтаборові вимоги по табору
vumohu_camp_kurinui = InlineKeyboardButton( text = " Таборові вимоги",
                                            url="https://docs.google.com/document/")
vumohu_kurinui.insert(vumohu_camp_kurinui)#кнопка вимоги по табору
vumohu_kurinui.insert(comeback_to_choise_kcamp)#кнопка повернутись на сторінку по курінному таборі
#вимоги до табору кнопки

Book_camp_f = InlineKeyboardMarkup(row_width=2)
Claim_dok = InlineKeyboardButton(text="Наказ на табір", callback_data="choose:claimdokkurinui") #кнопка наказу на табір
Book_camp_f.insert(Claim_dok)
list_camp = InlineKeyboardButton(text="Список учасників табору",
                                      callback_data="choose:listkurinuicap") #кнопка списку табору
Book_camp_f.insert(list_camp)

zgoloshenya_member_camp = InlineKeyboardButton(text="Зголошення учасника",
                                      callback_data="choose:zgoloshenyamembercamp ") #кнопка зголошення на табір
Book_camp_f.insert(zgoloshenya_member_camp)
Accept_camp = InlineKeyboardButton(text="Дозволи батьків ",
                                      callback_data="choose:Acceptcampkurinui") #кнопка дозволу батьків на табір
Book_camp_f.insert(Accept_camp)
insurance_camp = InlineKeyboardButton(text="Виписка про страхування",
                                      callback_data="choose:insurancekurinui") #кнопка страхування
Book_camp_f.insert(insurance_camp)
medical_reference_camp = InlineKeyboardButton(text="Медична довідка",
                                      callback_data="choose:medicalreferencecampkurinui") #кнопка медичні довідки
Book_camp_f.insert(medical_reference_camp)
medical_book_camp = InlineKeyboardButton(text="Медична книжка",
                                      callback_data="choose:medicalbookkurnui") #кнопка медичні довідки
Book_camp_f.insert(medical_book_camp)
copy_of_document_camp = InlineKeyboardButton(text="Копії документів",
                                      callback_data="choose:copyofdocumentkurinui") #кнопка копії документів
Book_camp_f.insert(copy_of_document_camp)
rules_camp = InlineKeyboardButton(text="Правильник табору",
                                      callback_data="choose:rulesofkurinui") #кнопка правильника табору
Book_camp_f.insert(rules_camp)
journal_of_safety_briefing = InlineKeyboardButton(text="Журнал з техніки безпеки",
                                      callback_data="choose:journalofsafetykurinui") #кнопка Журнал проведення інструктажу з техніки безпеки
Book_camp_f.insert(journal_of_safety_briefing)
sertuficat_CRT = InlineKeyboardButton(text="Сертифікат від ЦРТ",
                                      callback_data="choose:sertuficatcrt") #кнопка сертифікату від ЦРТ
Book_camp_f.insert(sertuficat_CRT)
sertuficat_PMD = InlineKeyboardButton(text="Сертифікати ДМД",
                                      callback_data="choose:sertuficatpmdkurinyui") #кнопка сертифікату від ЦРТ
Book_camp_f.insert(sertuficat_PMD)
comeback_to_choise_upy_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktokyrcamp")
Book_camp_f.insert(comeback_to_choise_upy_camp)#кнопка повернутись на сторінку по курінному таборі

#кнопки по книзі табору


med_dovika_kurin = InlineKeyboardMarkup(row_width=1)
med_dovika_kurin.insert(approve_from_contry)#кнопка інструкції заповнення
med_dovika_kurin.insert(template_med)#кнопка зразку мед довідки
comeback_to_choise_book_camp_kurinyui = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktobookkurinyui")
med_dovika_kurin.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
#кнопки по мед довідці

approve_parents_kurinui = InlineKeyboardMarkup(row_width=1)
approve_parents_kurinui.insert(parents_aprove_template)#шаблон дозволу від батьків
approve_parents_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
#кнопка дозволу від батьків

zgoloshenya_kurinui = InlineKeyboardMarkup(row_width=1)
zgoloshenya_kurinui.insert(zgoloshenya)#шаблон зголошення
zgoloshenya_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
# #кнопка зголошення на табір

list_kurinui = InlineKeyboardMarkup(row_width=1)
list_kurinui.insert(list_camper)#зразок списку табору
list_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
# #кнопка списку табору


insurance_kurinui = InlineKeyboardMarkup(row_width=1)
insurance_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
# кнопка по страхуванню

med_book_kurinui = InlineKeyboardMarkup(row_width=1)
med_book_kurinui.insert(med_book_dorosla)#кнопка  на постанову
med_book_kurinui.insert(med_book_buy)#кнопка  на приклад
med_book_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
# кнопка по медичну книжку


copui_doc__kurinui = InlineKeyboardMarkup(row_width=1)
copui_doc__kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
# кнопка про копії документів

rules_kurinui = InlineKeyboardMarkup(row_width=1)
rules_kurinui.insert(rules_camp)
rules_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
# кнопка про правильник табору

magazine_tehn_safe_kurinui = InlineKeyboardMarkup(row_width=1)
magazine_tehn_safe_kurinui.insert(magazine_tehn_safe)#кнопка приклад журнал провдення техніки безпеки
magazine_tehn_safe_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
# кнопка про журнал техніки безпеки

sertuficat_CRT_kurinui = InlineKeyboardMarkup(row_width=1)
sertuficat_CRT = InlineKeyboardButton(text="Зголоситись на вишкіл комендантів таборів",
                                      callback_data="choose:traink")
sertuficat_CRT_kurinui.insert(sertuficat_CRT)#кнопка зголоситись на вишкіл
sertuficat_CRT_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору

sertuficat_DMD_kurinui = InlineKeyboardMarkup(row_width=1)
sertuficat_DMD = InlineKeyboardButton(text="Зголоситись на курси",
                                      callback_data="choose:trainDMD")
sertuficat_DMD_kurinui.insert(sertuficat_DMD)#кнопка зголоситись на вишкіл
sertuficat_DMD_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
#сертифікат курсів ДМД


nakaz_kurinui = InlineKeyboardMarkup(row_width=1)
vymohu_pered_camp_kurinui =  InlineKeyboardButton(text="Передтаборові вимоги",
                                      url="https://docs.google.com/document/d/1etSqb0U-e4Wj4z231Ze-_SncMPpteEsxuspKrQEN"
                                          "2I0/edit?usp=sharing")#кнопка перед таборові вимоги
nakaz_kurinui.insert(vymohu_pered_camp_kurinui)
nakaz_kurinui.insert(comeback_to_choise_book_camp_kurinyui)#кнопка повернутись до книги табору
#наказ на табір
