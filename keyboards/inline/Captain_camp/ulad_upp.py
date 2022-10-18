from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.Captain_camp.book_camp import list_camper, magazine_tehn_safe

phatsch_camp = InlineKeyboardMarkup(row_width=1)
Claim_Gnizdech_camp = InlineKeyboardButton(text="Вимоги для проведення пташачих таборів",
                                  callback_data="choose:vymohuptaschch")#кнопка вимоги для проведення таборів
phatsch_camp.insert(Claim_Gnizdech_camp)
reporting_gnizdech_camp = InlineKeyboardButton(text="Зголошення пташачих таборів",
                                      callback_data="choose:reportingptaschch")#кнопка зголосити зголосити табір
phatsch_camp.insert(reporting_gnizdech_camp)
train_gnizdech = InlineKeyboardButton(text="Вишкіл комендантів пташачих таборів",
                                      callback_data="choose:trainptaschch")#кнопка про дошкіл комендантів
phatsch_camp.insert(train_gnizdech)
book_camp_gnizdech = InlineKeyboardButton(text="Книга табору",
                                      callback_data="choose:bookcampisptaschch")#кнопка відкрити книгу табору
phatsch_camp.insert(book_camp_gnizdech)
comeback_to_choise_ulad = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktoulad")# кнопка повернутись на обрання уладу

phatsch_camp.insert(comeback_to_choise_ulad)
# кнопки обрання по гніздовому таборі інформації



reporting_pschach_camp = InlineKeyboardMarkup(row_width=2)
comeback_to_choise_ptasch_camp = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktopschazch")
reporting_pschach_camp.insert(comeback_to_choise_ptasch_camp)
# кнопка по зголошенні пташачого табору таборі інформації

Book_camp_upp = InlineKeyboardMarkup(row_width=2)
Claim_dok = InlineKeyboardButton(text="Наказ на табір", callback_data="choose:ptaschachclaimdok") #кнопка наказу на табір
Book_camp_upp.insert(Claim_dok)
list_camp = InlineKeyboardButton(text="Список учасників табору",
                                      callback_data="choose:listcampptaschach") #кнопка списку табору
Book_camp_upp.insert(list_camp)
copy_of_document_camp = InlineKeyboardButton(text="Копії документів",
                                      callback_data="choose:copyofdocumentcampptaschach") #кнопка копії документів
Book_camp_upp.insert(copy_of_document_camp)
rules_camp = InlineKeyboardButton(text="Правильник табору",
                                      callback_data="choose:rulesofcampptaschach") #кнопка правильника табору
Book_camp_upp.insert(rules_camp)
journal_of_safety_briefing = InlineKeyboardButton(text="Журнал з техніки безпеки",
                                      callback_data="choose:journalofsafetybriefingptaschach") #кнопка Журнал проведення інструктажу з техніки безпеки
Book_camp_upp.insert(journal_of_safety_briefing)
sertuficat_PMD = InlineKeyboardButton(text="Cертифікати ДМД",
                                      callback_data="choose:sertuficatpmdptaschach") #кнопка сертифікату від ЦРТ
Book_camp_upp.insert(sertuficat_PMD)
Book_camp_upp.insert(comeback_to_choise_ptasch_camp)#кнопка повернутись на сторінку по пташачому таборі

vumohu_pschazch = InlineKeyboardMarkup(row_width=1)
pered_camp_pschazch = InlineKeyboardButton(text=" Передтаборові вимоги",
                                           url="https://docs.google.com/document/d/1etSqb0U-e4Wj4z231Ze-_SncMPp"
                                               "teEsxuspKrQEN2I0/edit?usp=sharing")
vumohu_pschazch.insert(pered_camp_pschazch)#кнопка передтаборові вимоги по табору
vumohu_camp_pschazch = InlineKeyboardButton( text = " Таборові вимоги",
                                            url="https://docs.google.com/document/")
vumohu_pschazch.insert(vumohu_camp_pschazch)#кнопка вимоги по табору
vumohu_pschazch.insert(comeback_to_choise_ptasch_camp)#кнопка повернутись на сторінку по курінному таборі
#вимоги до табору кнопки

traning_for_captain_camp_ptascach = InlineKeyboardMarkup(row_width=1)
traning_for_captain_campkyrbutton_March_15_16= InlineKeyboardButton(text=".... ",
                                      url="https://docs.google.com/forms/d/1X1jp3OyPEnK8mpcgue"
                                          "Jc5G9PfVVI0chqQ7mIx0911_Y/edit")
traning_for_captain_camp_ptascach.insert(traning_for_captain_campkyrbutton_March_15_16)# кнопка зголошення на дошкіл комендантів гніздових
traning_for_captain_camp_ptascach.insert(comeback_to_choise_ptasch_camp) #кнопка повернутись на сторінку по курінному таборі
# кнопки зголошення на вишкіл комендантів


comeback_to_choise_book_ptaschui= InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:returntobookpschazch  ")

list_ptaschui = InlineKeyboardMarkup(row_width=1)
list_ptaschui.insert(list_camper)#зразок списку табору
list_ptaschui.insert(comeback_to_choise_book_ptaschui)#кнопка повернутись до книги табору
# #кнопка списку табору


copui_doc__ptaschui = InlineKeyboardMarkup(row_width=1)
copui_doc__ptaschui.insert(comeback_to_choise_book_ptaschui)#кнопка повернутись до книги табору
# кнопка про копії документів

rules_ptaschui = InlineKeyboardMarkup(row_width=1)
rules_ptaschui.insert(rules_camp)
rules_ptaschui.insert(comeback_to_choise_book_ptaschui)#кнопка повернутись до книги табору
# кнопка про правильник табору

magazine_tehn_safe_ptaschui= InlineKeyboardMarkup(row_width=1)
magazine_tehn_safe_ptaschui.insert(magazine_tehn_safe)#кнопка приклад журнал провдення техніки безпеки
magazine_tehn_safe_ptaschui.insert(comeback_to_choise_book_ptaschui)#кнопка повернутись до книги табору
# кнопка про журнал техніки безпеки


sertuficat_DMD_ptaschui = InlineKeyboardMarkup(row_width=1)
sertuficat_DMD = InlineKeyboardButton(text="Зголоситись на курси",
                                      callback_data="choose:trainDMD")
sertuficat_DMD_ptaschui.insert(sertuficat_DMD)#кнопка зголоситись на вишкіл
sertuficat_DMD_ptaschui.insert(comeback_to_choise_book_ptaschui)#кнопка повернутись до книги табору
#сертифікат курсів ДМД


nakaz_ptaschui= InlineKeyboardMarkup(row_width=1)
nakaz_ptaschui.insert(pered_camp_pschazch)
nakaz_ptaschui.insert(comeback_to_choise_book_ptaschui)#кнопка повернутись до книги табору
#наказ на табір