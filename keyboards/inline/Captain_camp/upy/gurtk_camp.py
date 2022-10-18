from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.Captain_camp.book_camp import approve_from_contry, template_med, parents_aprove_template, \
    zgoloshenya, med_book_dorosla, med_book_buy, magazine_tehn_safe, list_camper
from keyboards.inline.Captain_camp.upy.kyr_camp_upy import comeback_to_choise_book_camp_kurinyui

gurtkov_camp = InlineKeyboardMarkup(row_width=1)
Claim_camp_g = InlineKeyboardButton(text="Вимоги для проведення гурткових таборів 💬📌",
                                  callback_data="choose:Claimcampgurtkovui")#кнопка вимоги для проведення таборів
gurtkov_camp.insert(Claim_camp_g)
reporting_camp_g = InlineKeyboardButton(text="Зголошення гурткових таборів  🆘📢",
                                          callback_data="choose:zgoloshenyagurt")#кнопка зголосити гуртковий табір
gurtkov_camp.insert(reporting_camp_g)
train_k = InlineKeyboardButton(text="Вишкіл комендантів гурткових таборів ⏳📚",
                                          callback_data="choose:traingurt")#кнопка про вишкіл коменданта гурткових таборів
gurtkov_camp.insert(train_k)
book_camp_g = InlineKeyboardButton(text="Книга табору 📒❗️",
                                          callback_data="choose:bookcampgurtk")#кнопка відкрити книгу гурткового табору
gurtkov_camp.insert(book_camp_g)
comeback_to_choise_upy_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktoupycamp")# кнопка повернутись на обрання курінного
# чи гурткового табору
gurtkov_camp.insert(comeback_to_choise_upy_camp)
# кнопки обрання по курінному таборі інформації



gurtkov_camp_come_back = InlineKeyboardMarkup(row_width=1)
comeback_to_choise_gurt_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:backtogurtkovyh")
gurtkov_camp_come_back.insert(comeback_to_choise_gurt_camp)
# кнопка повернутись до гурткового табору



train_gurtkovyu = InlineKeyboardMarkup(row_width=1)
first_dt = InlineKeyboardButton(text="27-28 березня",
                                     url="https://docs.google.com/forms/d/e/1FAIpQLSemlzXyKk3HNjmxky4bD7HzPKmflK37Sh"
                                         "cAUrnPDSc8Y-V1xQ/viewform")# кнопка вибрати першу дату
train_gurtkovyu.insert(first_dt) # кнопка вибрати другу дату
train_gurtkovyu.insert(comeback_to_choise_gurt_camp)# кнопка повернутись до гурткового табору
# кнопки по зголошенню на вишкіл комендантів гурткових таборів


vumohu_gurtkovyu = InlineKeyboardMarkup(row_width=1)
pered_camp_gurtkovyu = InlineKeyboardButton(text=" Передтаборові вимоги",
                                           url="https://docs.google.com/document/d/1WupS3fZrnR9nmv9s7OCXI8TzRarD6qk"
                                               "tVNh5bSIXVoY/edit?usp=sharing")
vumohu_gurtkovyu.insert(pered_camp_gurtkovyu)#кнопка передтаборові вимоги по табору
vumohu_camp_gurtkovyu = InlineKeyboardButton( text = " Таборові вимоги",
                                            url="https://docs.google.com/document/")
vumohu_gurtkovyu.insert(vumohu_camp_gurtkovyu)#кнопка вимоги по табору
vumohu_gurtkovyu.insert(comeback_to_choise_gurt_camp)#кнопка повернутись на сторінку по курінному таборі
#вимоги до табору кнопки

Book_camp_gurt = InlineKeyboardMarkup(row_width=2)
Claim_dok = InlineKeyboardButton(text="Наказ на табір", callback_data="choose:claimdokgurtkovui") #кнопка наказу на табір
Book_camp_gurt.insert(Claim_dok)
list_camp = InlineKeyboardButton(text="Список учасників табору",
                                      callback_data="choose:listgurtkovui") #кнопка списку табору
Book_camp_gurt.insert(list_camp)

zgoloshenya_member_camp = InlineKeyboardButton(text="Зголошення учасника  ",
                                      callback_data="choose:zgoloshenygurtkovui ") #кнопка зголошення на табір
Book_camp_gurt.insert(zgoloshenya_member_camp)
Accept_camp = InlineKeyboardButton(text="Дозволи батьків ",
                                      callback_data="choose:Acceptgurtkovui") #кнопка дозволу батьків на табір
Book_camp_gurt.insert(Accept_camp)
insurance_camp = InlineKeyboardButton(text="Виписка про страхування",
                                      callback_data="choose:insurancegurtkovui") #кнопка страхування
Book_camp_gurt.insert(insurance_camp)
medical_reference_camp = InlineKeyboardButton(text="Медична довідка ",
                                      callback_data="choose:meddocumentgurtkovoi") #кнопка медичні довідки
Book_camp_gurt.insert(medical_reference_camp)
medical_book_camp = InlineKeyboardButton(text="Медична книжка ",
                                      callback_data="choose:medicalbookgurtkovui") #кнопка медичні довідки
Book_camp_gurt.insert(medical_book_camp)
copy_of_document_camp = InlineKeyboardButton(text="Копії документів",
                                      callback_data="choose:copyofdocumentgurtkovui") #кнопка копії документів
Book_camp_gurt.insert(copy_of_document_camp)
rules_camp = InlineKeyboardButton(text="Правильник табору",
                                      callback_data="choose:rulesofgurtkovui") #кнопка правильника табору
Book_camp_gurt.insert(rules_camp)
journal_of_safety_briefing = InlineKeyboardButton(text="Журнал з техніки безпеки",
                                      callback_data="choose:journalofsafetgurtkovui") #кнопка Журнал проведення інструктажу з техніки безпеки
Book_camp_gurt.insert(journal_of_safety_briefing)
sertuficat_PMD_gurt = InlineKeyboardButton(text="Сертифікат ДМД",
                                      callback_data="choose:sertuficatpmdgurtkovui") #кнопка сертифікату від ЦРТ
Book_camp_gurt.insert(sertuficat_PMD_gurt)
Book_camp_gurt.insert(comeback_to_choise_gurt_camp)#кнопка повернутись на сторінку по курінному таборі
#кнопки для книги табору


med_dovika_gurtk = InlineKeyboardMarkup(row_width=1)
med_dovika_gurtk.insert(approve_from_contry)#кнопка інструкції заповнення
med_dovika_gurtk.insert(template_med)#кнопка зразку мед довідки
return_to_book_camp_gurtk = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:returntobookgurtkovui")
med_dovika_gurtk.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
#кнопки по мед довідці

approve_parents_gurtkoui = InlineKeyboardMarkup(row_width=1)
approve_parents_gurtkoui.insert(parents_aprove_template)#шаблон дозволу від батьків
approve_parents_gurtkoui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
#кнопка дозволу від батьків

zgoloshenya_gurtkovui = InlineKeyboardMarkup(row_width=1)
zgoloshenya_gurtkovui.insert(zgoloshenya)#шаблон зголошення
zgoloshenya_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
#кнопка зголошення на табір

list_gurtkovui = InlineKeyboardMarkup(row_width=1)
list_gurtkovui.insert(list_camp)#зразок списку табору
list_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
# #кнопка списку табору

insurance_gurtkovui= InlineKeyboardMarkup(row_width=1)
insurance_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
# кнопка по страхуванню

med_book_gurtkovui = InlineKeyboardMarkup(row_width=1)
med_book_gurtkovui.insert(med_book_dorosla)#кнопка  на постанову
med_book_gurtkovui.insert(med_book_buy)#кнопка  на приклад
med_book_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
# кнопка по медичну книжку


copui_doc__gurtkovui = InlineKeyboardMarkup(row_width=1)
copui_doc__gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
# кнопка про копії документів

rules_gurtkovui = InlineKeyboardMarkup(row_width=1)
rules_gurtkovui.insert(rules_camp)
rules_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
# кнопка про правильник табору

magazine_tehn_safe_gurtkovui = InlineKeyboardMarkup(row_width=1)
magazine_tehn_safe_gurtkovui.insert(magazine_tehn_safe)#кнопка приклад журнал провдення техніки безпеки
magazine_tehn_safe_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
# кнопка про журнал техніки безпеки

nakaz_gurtkovui= InlineKeyboardMarkup(row_width=1)
nakaz_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
#наказ на табір

list_gurtkovui = InlineKeyboardMarkup(row_width=1)
list_gurtkovui.insert(list_camper)#зразок списку табору
list_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
# #кнопка списку табору


nakaz_gurtkovui = InlineKeyboardMarkup(row_width=1)
vymohu_pered_camp_gurtkovui =  InlineKeyboardButton(text="Передтаборові вимоги",
                                      url="https://docs.google.com/document/d/1WupS3fZrnR9nmv9s7OCXI8TzRarD6qktVNh5bSI"
                                          "XVoY/edit?usp=sharing")#кнопка перед таборові вимоги
nakaz_gurtkovui.insert(vymohu_pered_camp_gurtkovui)
nakaz_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
#наказ на табір

sertuficat_DMD_gurtkovui = InlineKeyboardMarkup(row_width=1)
sertuficat_DMD = InlineKeyboardButton(text="Зголоситись на курси",
                                      callback_data="choose:trainDMD")
sertuficat_DMD_gurtkovui.insert(sertuficat_DMD)#кнопка зголоситись на вишкіл
sertuficat_DMD_gurtkovui.insert(return_to_book_camp_gurtk)#кнопка повернутись до книги табору
#сертифікат курсів ДМД