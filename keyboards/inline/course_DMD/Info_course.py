from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Info_to_course=   InlineKeyboardMarkup(row_width=3)
Februar = InlineKeyboardButton(text="Лютий", callback_data="choose:Februar")# кнопка вибрати лютий
Info_to_course.insert(Februar)
March = InlineKeyboardButton(text= "Березень", callback_data="choose:March")# кнопка вибрати березень
Info_to_course.insert(March)
April = InlineKeyboardButton(text="Квітень", callback_data="choose:April")# кнопка вибрати квітень
Info_to_course.insert(April)
MAl_hepl = InlineKeyboardButton(text="Мальтіська служба допомоги",
                                url ="https://www.facebook.com/%D0%9C%D0%B0%D0%BB%D1%8C%D1%82%D1%96%D0%B9%D1%81%D1%8C%D0"
                                     "%BA%D0%B0-%D1%81%D0%BB%D1%83%D0%B6%D0%B1%D0%B0-%D0%B4%D0%BE%D0%BF%D0%BE%D0%BC%D0%"
                                     "BE%D0%B3%D0%B8-326347987446539/")# кнопка вибрати лінк на мальтійську службу допомоги
Info_to_course.insert(MAl_hepl)



