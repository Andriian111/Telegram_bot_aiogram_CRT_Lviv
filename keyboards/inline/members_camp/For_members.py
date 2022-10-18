from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

members_camp = InlineKeyboardMarkup(row_width=1)
outfit = InlineKeyboardButton(text="Рекомендований особистий виряд 🎒", callback_data="choose:outfit")# кнопка вибрати виряд на табір
members_camp.insert(outfit)
documents_for_child = InlineKeyboardButton(text= "Список документів на табір 📂", callback_data="choose:documentsforchild")# кнопка вибрати упн
members_camp.insert(documents_for_child)
Covid_save_for_child = InlineKeyboardButton(text="Рекомендації по безпеці від covid-19 😷",
                                     url ="https://docs.google.com/document/d/1i22S2QCer_TL-VVZAZOF8Whoq_50X"
                                          "e-C-RHnAJl5RHE/edit")# кнопка вибрати коронавірусну безпеку
members_camp.insert(Covid_save_for_child)


