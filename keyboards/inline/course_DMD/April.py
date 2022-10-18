from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

April_course=   InlineKeyboardMarkup(row_width=3)
comeback_to_choise_month = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktochoisemonth")
April_course.insert(comeback_to_choise_month) #кнопка повернутись на сторінку обрання місяця