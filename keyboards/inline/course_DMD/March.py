from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

march_course=   InlineKeyboardMarkup(row_width=3)
First_date = InlineKeyboardButton(text="....", callback_data="choose:Februar")# кнопка вибрати лютий
march_course.insert(First_date)
Second_date = InlineKeyboardButton(text= "...", callback_data="choose:March")# кнопка вибрати березень
march_course.insert(Second_date)
Third_date = InlineKeyboardButton(text="...", callback_data="choose:April")# кнопка вибрати квітень
march_course.insert(Third_date)
comeback_to_choise_month = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktochoisemonth")
march_course.insert(comeback_to_choise_month) #кнопка повернутись на сторінку обрання місяця