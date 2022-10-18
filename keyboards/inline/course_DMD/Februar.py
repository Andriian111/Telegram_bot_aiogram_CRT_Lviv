from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Februar_course=   InlineKeyboardMarkup(row_width=4)
First_date1 = InlineKeyboardButton(text="22-23", url="https://t.me/joinchat/EIXBmHxSyF_n617b")# кнопка вибрати лютий
Februar_course.insert(First_date1)
Second_date2 = InlineKeyboardButton(text= "25-26", url="https://t.me/joinchat/HhaekZkklnj63_0_")# кнопка вибрати березень
Februar_course.insert(Second_date2)
Third_date3 = InlineKeyboardButton(text="27", url="https://t.me/joinchat/IOVZ6dUizPgjZTpC")# кнопка вибрати квітень
Februar_course.insert(Third_date3)
Third_date4 = InlineKeyboardButton(text="28 ", url="https://t.me/joinchat/HjX5DKYAGFU7C0pm")# кнопка вибрати квітень
Februar_course.insert(Third_date4)
comeback_to_choise_month = InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:comebacktochoisemonth")
Februar_course.insert(comeback_to_choise_month) #кнопка повернутись на сторінку обрання місяця
