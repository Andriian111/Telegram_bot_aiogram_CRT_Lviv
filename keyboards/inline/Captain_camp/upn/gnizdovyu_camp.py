from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.Captain_camp.book_camp import approve_from_contry, template_med, parents_aprove_template, \
    zgoloshenya, list_camper, med_book_dorosla, med_book_buy, magazine_tehn_safe

gniz_camp = InlineKeyboardMarkup(row_width=1)
Claim_G_camp = InlineKeyboardButton(text="Вимоги для проведення таборів",
                                    callback_data="choose:vumohugnizdovui")#кнопка вимоги для проведення таборів
gniz_camp.insert(Claim_G_camp)
reporting_gnizd_camp = InlineKeyboardButton(text="Зголошення гніздових таборів",
                                      callback_data="choose:reportinggnizdcamp")#кнопка зголосити зголосити табір
gniz_camp.insert(reporting_gnizd_camp)
train_gnizd = InlineKeyboardButton(text="Дошкіл комендантів гніздових таборів",
                                      callback_data="choose:traingnizd")#кнопка про дошкіл комендантів
gniz_camp.insert(train_gnizd)
book_camp_gnizd = InlineKeyboardButton(text="Книга табору",
                                      callback_data="choose:bookcampisgnizd")#кнопка відкрити книгу табору
gniz_camp.insert(book_camp_gnizd)
comeback_to_choise_upn_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktoupncamp")# кнопка повернутись на обрання гніздового чи ройового табору
gniz_camp.insert(comeback_to_choise_upn_camp)
# кнопки обрання по гніздовому таборі інформації

comeback_tp_gnizd_camp = InlineKeyboardMarkup(row_width=1)
comeback_to_choise_gnizd_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktognizdcamp")
comeback_tp_gnizd_camp.insert(comeback_to_choise_gnizd_camp)
# кнопка повернення на обрання по  гніздовому таборі інформації

vumohu_gnizdovui = InlineKeyboardMarkup(row_width=1)
pered_camp_gnizdovui = InlineKeyboardButton(text=" Передтаборові вимоги",
                                           url="https://docs.google.com/document/d/1etSqb0U-e4Wj4z231Ze-_SncMPp"
                                               "teEsxuspKrQEN2I0/edit?usp=sharing")
vumohu_gnizdovui.insert(pered_camp_gnizdovui)#кнопка передтаборові вимоги по табору
vumohu_camp_kurinui = InlineKeyboardButton( text = " Таборові вимоги",
                                            url="https://docs.google.com/document/")
vumohu_gnizdovui.insert(vumohu_camp_kurinui)#кнопка вимоги по табору
vumohu_gnizdovui.insert(comeback_to_choise_gnizd_camp)#кнопка повернутись на сторінку по курінному таборі
#вимоги до табору кнопки

Book_camp_upn = InlineKeyboardMarkup(row_width=2)
Claim_dok = InlineKeyboardButton(text="Наказ на табір", callback_data="choose:claimdokgnizdovui",) #кнопка наказу на табір
Book_camp_upn.insert(Claim_dok)
list_camp = InlineKeyboardButton(text="Список учасників табору",
                                      callback_data="choose:listcampgnizdovui") #кнопка списку табору
Book_camp_upn.insert(list_camp)

Accept_camp = InlineKeyboardButton(text="Дозволи  батьків ",
                                      callback_data="choose:Acceptgnizdovui ") #кнопка дозволу батьків на табір
Book_camp_upn.insert(Accept_camp)
insurance_camp = InlineKeyboardButton(text="Виписка про страхування",
                                      callback_data="choose:insurancegnizdovui ") #кнопка страхування
Book_camp_upn.insert(insurance_camp)
medical_reference_camp = InlineKeyboardButton(text="Медична довідка",
                                      callback_data="choose:medicalreferencegnizdovui ") #кнопка медичні довідки
Book_camp_upn.insert(medical_reference_camp)
medical_book_camp = InlineKeyboardButton(text="Медична книжка ",
                                      callback_data="choose:medicalbookcampgnizdovui ") #кнопка медичні книга
Book_camp_upn.insert(medical_book_camp)
copy_of_document_camp = InlineKeyboardButton(text="Копії документів",
                                      callback_data="choose:copyofdocumentgnizdovui ") #кнопка копії документів
Book_camp_upn.insert(copy_of_document_camp)
rules_camp = InlineKeyboardButton(text="Правильник табору",
                                      callback_data="choose:rulesofgnizdovui ") #кнопка правильника табору
Book_camp_upn.insert(rules_camp)
journal_of_safety_briefing = InlineKeyboardButton(text="Журнал з техніки безпеки",
                                      callback_data="choose:journalofsafegnizdovui ") #кнопка Журнал проведення інструктажу з техніки безпеки
Book_camp_upn.insert(journal_of_safety_briefing)
sertuficat_PMD = InlineKeyboardButton(text="Cертифікати ДМД",
                                      callback_data="choose:sertuficatpmdgnizdovui ") #кнопка сертифікату від ЦРТ
Book_camp_upn.insert(sertuficat_PMD)
comeback_to_gnizd_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktognizdgnizdovui ")
Book_camp_upn.insert(comeback_to_gnizd_camp)#кнопка повернутись на сторінку по гніздовому таборі


traning_for_captain_campgnizd = InlineKeyboardMarkup(row_width=1)
traning_for_captain_campkyrbutton_March_15_16= InlineKeyboardButton(text=".... ",
                                      url="https://docs.google.com/forms/d/1X1jp3OyPEnK8mpcgue"
                                          "Jc5G9PfVVI0chqQ7mIx0911_Y/edit")
traning_for_captain_campgnizd.insert(traning_for_captain_campkyrbutton_March_15_16)# кнопка зголошення на дошкіл комендантів гніздових
traning_for_captain_campgnizd.insert(comeback_to_gnizd_camp) #кнопка повернутись на сторінку по курінному таборі
# кнопки зголошення на вишкіл комендантів





med_dovika_gnizdovui = InlineKeyboardMarkup(row_width=1)
med_dovika_gnizdovui.insert(approve_from_contry)#кнопка інструкції заповнення
med_dovika_gnizdovui.insert(template_med)#кнопка зразку мед довідки
comeback_to_choise_book_camp_rouovui = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktobookgnizdovui ")
med_dovika_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#кнопки по мед довідці

approve_parents_gnizdovui = InlineKeyboardMarkup(row_width=1)
approve_parents_gnizdovui.insert(parents_aprove_template)#шаблон дозволу від батьків
approve_parents_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#кнопка дозволу від батьків

zgoloshenya_gnizdovui = InlineKeyboardMarkup(row_width=1)
zgoloshenya_gnizdovui.insert(zgoloshenya)#шаблон зголошення
zgoloshenya_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# #кнопка зголошення на табір

list_gnizdovui = InlineKeyboardMarkup(row_width=1)
list_gnizdovui.insert(list_camper)#зразок списку табору
list_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# #кнопка списку табору


insurance_gnizdovui = InlineKeyboardMarkup(row_width=1)
insurance_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка по страхуванню

med_book_gnizdovui = InlineKeyboardMarkup(row_width=1)
med_book_gnizdovui.insert(med_book_dorosla)#кнопка  на постанову
med_book_gnizdovui.insert(med_book_buy)#кнопка  на приклад
med_book_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка по медичну книжку


copui_doc__gnizdovui = InlineKeyboardMarkup(row_width=1)
copui_doc__gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка про копії документів

rules_gnizdovui = InlineKeyboardMarkup(row_width=1)
rules_gnizdovui.insert(rules_camp)
rules_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка про правильник табору

magazine_tehn_safe_gnizdovui= InlineKeyboardMarkup(row_width=1)
magazine_tehn_safe_gnizdovui.insert(magazine_tehn_safe)#кнопка приклад журнал провдення техніки безпеки
magazine_tehn_safe_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
# кнопка про журнал техніки безпеки


sertuficat_DMD_gnizdovui = InlineKeyboardMarkup(row_width=1)
sertuficat_DMD = InlineKeyboardButton(text="Зголоситись на курси",
                                      callback_data="choose:trainDMD")
sertuficat_DMD_gnizdovui.insert(sertuficat_DMD)#кнопка зголоситись на вишкіл
sertuficat_DMD_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#сертифікат курсів ДМД


nakaz_gnizdovui= InlineKeyboardMarkup(row_width=1)
vymohu_pered_camp_gnizdovui =  InlineKeyboardButton(text="Передтаборові вимоги",
                                      url="https://docs.google.com/document/d/1etSqb0U-e4Wj4z231Ze-_SncMPpteEsxuspKrQEN"
                                          "2I0/edit?usp=sharing")#кнопка перед таборові вимоги
nakaz_gnizdovui.insert(vymohu_pered_camp_gnizdovui)
nakaz_gnizdovui.insert(comeback_to_choise_book_camp_rouovui)#кнопка повернутись до книги табору
#наказ на табір