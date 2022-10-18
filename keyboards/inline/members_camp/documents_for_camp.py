from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.Captain_camp.book_camp import approve_from_contry, template_med, parents_aprove_template

documents_members =   InlineKeyboardMarkup(row_width=1)
zgoloshenya = InlineKeyboardButton(text="Зголошення на табір", callback_data="choose:zgoloshenyakids")# кнопка вибрати виряд на табір
documents_members.insert(zgoloshenya)
approve_parents = InlineKeyboardButton(text= "Дозвіл батьків про участь у таборі", callback_data="choose:Acceptcampkids")# кнопка вибрати упн
documents_members.insert(approve_parents)
med_dovidka = InlineKeyboardButton(text="Медична довідка", callback_data="choose:medicaldockids")# кнопка вибрати коронавірусну безпеку
documents_members.insert(med_dovidka)
pasport = InlineKeyboardButton(text="Копія документів ", callback_data="choose:copyofdocumentkids")# кнопка вибрати упп
documents_members.insert(pasport)
last_store = InlineKeyboardButton(text="Повернутись на попередню сторінку", callback_data="choose:laststore")# кнопка поврентись до таборового помічника
documents_members.insert(last_store)

come_back_to_kids_documents = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                                   callback_data="choose:comebackkidsdocuments")# кнопка повернутись до документів


zgoloshenya_kids= InlineKeyboardMarkup(row_width=1)
zgoloshenya_kids.insert(zgoloshenya)#шаблон зголошення
zgoloshenya_kids.insert(come_back_to_kids_documents)#кнопка повернутись до документів
# #кнопка зголошення на табір

approve_parents_kids = InlineKeyboardMarkup(row_width=1)
approve_parents_kids.insert(parents_aprove_template)#шаблон дозволу від батьків
approve_parents_kids.insert(come_back_to_kids_documents)#кнопка повернутись до документів
#кнопка дозволу від батьків

med_dovika_kids = InlineKeyboardMarkup(row_width=1)
med_dovika_kids.insert(approve_from_contry)#кнопка інструкції заповнення
med_dovika_kids.insert(come_back_to_kids_documents)#кнопка повернутись до документів
#кнопки по мед довідці

copui_doc__kids = InlineKeyboardMarkup(row_width=1)
copui_doc__kids.insert(come_back_to_kids_documents)#кнопка повернутись до документів
# кнопка про копії документів