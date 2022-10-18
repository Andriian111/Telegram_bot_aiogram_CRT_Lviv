from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

covid_members =   InlineKeyboardMarkup(row_width=1)
list_of_covid = InlineKeyboardButton(text="Рекомендації по безпеці від коронавірусу 😷",
                                     url ="https://docs.google.com/document/d/1i22S2QCer_TL-VVZAZOF8Whoq_50X"
                                          "e-C-RHnAJl5RHE/edit")# кнопка відкрити про коронавірусну безпеку дітей
covid_members.insert(list_of_covid)
last_store = InlineKeyboardButton(text="Повернутись на попередню сторінку", callback_data="choose:laststore")# кнопка поврентись до таборового помічника
covid_members.insert(last_store)



