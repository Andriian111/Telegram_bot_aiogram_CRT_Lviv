from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

place_of_camping = InlineKeyboardMarkup(row_width=1)
procedure_place = InlineKeyboardButton(text="Порядок дій для пошуку місця табору",
                                      url="https://www.facebook.com/kontra.skob/photos/a.460037351199"
                                          "763/509409149595916/?type=3&theater&ifg=1")# кнопка щоб дізнатись порядок дій
place_of_camping.insert(procedure_place)
place_from_pl_plast_banka = InlineKeyboardButton(text="Місця для таборів на Пластовій Банці",
                                      url="https://www.facebook.com/kontra.skob/photos/a.460037351199"
                                          "763/509409149595916/?type=3&theater&ifg=1")# кнопка щоб місця таборів від пластвої банки
place_of_camping.insert(place_from_pl_plast_banka)


reurn_to_list_of_help= InlineKeyboardButton(text="Повернутись на попередню сторінку",
                                      callback_data="choose:reurnlistofhelp  ")
place_of_camping.insert(reurn_to_list_of_help)
