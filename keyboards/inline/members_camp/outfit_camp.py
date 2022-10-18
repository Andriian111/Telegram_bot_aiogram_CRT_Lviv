from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

out_fit_for_cammp = InlineKeyboardMarkup(row_width=4)
Naplichnyk = InlineKeyboardButton(text="Наплічник 🎒", url="https://plastovabanka.org.ua/gutirka/yak-vybraty-na"
                                                                  "plechnyk/")# кнопка вибрати виряд на табір
out_fit_for_cammp.insert(Naplichnyk)
Spalnyk = InlineKeyboardButton(text= "Спальник", url="https://www.gorgany.com/pro/how-to-choose-sleeping-b"
                                                               "ag/")# кнопка вибрати упн
out_fit_for_cammp.insert(Spalnyk)
Karemat = InlineKeyboardButton(text="Каремат", url="https://www.gorgany.com/pro/how-to-choose-mat/")# кнопка вибрати коронавірусну безпеку
out_fit_for_cammp.insert(Karemat)
boots = InlineKeyboardButton(text="Взуття", url="https://plastovabanka.org.ua/gutirka/vzuttya-dlya-mandriv"
                                                           "ok-yak-vybraty-i-yak-nosyty/")# кнопка вибрати коронавірусну безпеку
out_fit_for_cammp.insert(boots)



last_store = InlineKeyboardButton(text="Повернутись на попередню сторінку", callback_data="choose:laststore")# кнопка поврентись до таборового помічника
out_fit_for_cammp.insert(last_store)